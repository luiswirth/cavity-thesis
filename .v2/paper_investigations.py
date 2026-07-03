"""
Self-contained numpy replication of the maxwellgp plane-wave feature map,
to investigate two paper-backlog claims:

  PAPER-G  basis-rotation robustness: the transverse basis (e1,e2) per
           spectral direction is fixed only up to a rotation; the kernel /
           GP posterior must not depend on that choice (with W = I).

  PAPER-D  condition-number of A = W^-1 + Phi Phi^H / sigma_n^2 (W = I):
           replace the heuristic "cond ~ 1/sigma_n^2" with the real
           dependence on the feature-Gram spectrum.

Feature construction mirrors maxwellgp/kernel.py::MaxwellFeatureMap exactly.
"""
import numpy as np

np.random.seed(0)


def fibonacci_sphere(n):
    k = np.arange(n) + 0.5
    golden = (1.0 + np.sqrt(5.0)) / 2.0
    phi = 2.0 * np.pi / golden
    z = 1.0 - 2.0 * k / n
    r = np.sqrt(np.clip(1.0 - z * z, 0.0, None))
    theta = phi * k
    return np.stack([r * np.cos(theta), r * np.sin(theta), z], axis=-1)


def normalize(v, axis=-1):
    return v / (np.linalg.norm(v, axis=axis, keepdims=True) + 1e-12)


def standard_basis(kdirs):
    """Deterministic transverse frame from kernel.py: pivot = axis least aligned with k."""
    piv_idx = np.argmin(np.abs(kdirs), axis=1)
    pivot = np.eye(3)[piv_idx]
    e1 = normalize(np.cross(kdirs, pivot))
    e2 = normalize(np.cross(kdirs, e1))
    return e1, e2


def rotate_basis(e1, e2, thetas):
    """Rotate each transverse frame by its own angle theta within the plane."""
    c, s = np.cos(thetas)[:, None], np.sin(thetas)[:, None]
    return c * e1 + s * e2, -s * e1 + c * e2


def random_transverse_basis(kdirs):
    """A completely independent orthonormal transverse frame (random pivot)."""
    rand = np.random.randn(*kdirs.shape)
    e1 = normalize(np.cross(kdirs, rand))
    e2 = normalize(np.cross(kdirs, e1))
    return e1, e2


def full_features(X, kdirs, e1, e2, k):
    """(F, 6N) complex feature matrix, full 6-component trace."""
    pols = np.stack([e1, e2], axis=1)            # (R,2,3)
    kvec = kdirs * k
    cross = np.cross(kvec[:, None, :], pols)      # (R,2,3)
    E0 = -cross
    B0 = np.cross(kdirs[:, None, :], cross)       # (R,2,3)
    coeff6 = np.concatenate([E0, B0], axis=-1).astype(complex)  # (R,2,6)
    phases = np.exp(1j * (X @ kvec.T))            # (N,R)
    feat = np.einsum("rpc,nr->rpnc", coeff6, phases)
    R = kdirs.shape[0]
    return feat.reshape(R * 2, X.shape[0] * 6)


def tangential_features(Xn, kdirs, e1, e2, k):
    """(F, 3N) complex feature matrix, tangential trace. Xn = [point(3), normal(3)]."""
    pols = np.stack([e1, e2], axis=1)
    kvec = kdirs * k
    E0 = -np.cross(kvec[:, None, :], pols)        # (R,2,3)
    n = Xn[:, 3:][None, None, :, :]               # (1,1,N,3)
    E0b = E0[:, :, None, :]                        # (R,2,1,3)
    tE = E0b - np.sum(E0b * n, axis=-1, keepdims=True) * n
    phases = np.exp(1j * (Xn[:, :3] @ kvec.T))     # (N,R)
    feat = np.einsum("rpnc,nr->rpnc", tE, phases)
    R = kdirs.shape[0]
    return feat.reshape(R * 2, Xn.shape[0] * 3)


# ---------------------------------------------------------------------------
print("=" * 70)
print("PAPER-G : basis-rotation invariance of the kernel (W = I)")
print("=" * 70)
k = 2.0
n_spectral = 256
kdirs = normalize(fibonacci_sphere(n_spectral))

# random interior evaluation points inside the sphere R=4
N = 40
X = np.random.randn(N, 3)
X = X / np.linalg.norm(X, axis=1, keepdims=True) * (np.random.rand(N, 1) * 3.5)

e1, e2 = standard_basis(kdirs)
e1r, e2r = rotate_basis(e1, e2, thetas=np.random.rand(n_spectral) * 2 * np.pi)
e1x, e2x = random_transverse_basis(kdirs)

Phi_std = full_features(X, kdirs, e1, e2, k)
Phi_rot = full_features(X, kdirs, e1r, e2r, k)
Phi_rnd = full_features(X, kdirs, e1x, e2x, k)

# kernel Gram (the ONLY thing the GP posterior sees, with W=I): G = Phi^H Phi
G_std = Phi_std.conj().T @ Phi_std
G_rot = Phi_rot.conj().T @ Phi_rot
G_rnd = Phi_rnd.conj().T @ Phi_rnd
scale = np.abs(G_std).max()
print(f"kernel Gram Phi^H Phi   (6N x 6N), scale={scale:.3e}")
print(f"  rel diff  standard vs rotated-in-plane : {np.abs(G_std-G_rot).max()/scale:.2e}")
print(f"  rel diff  standard vs random frame     : {np.abs(G_std-G_rnd).max()/scale:.2e}")

# also confirm the per-direction transverse projector is basis-independent
Pi_std = np.einsum("rc,rd->rcd", e1, e1) + np.einsum("rc,rd->rcd", e2, e2)
Pi_rnd = np.einsum("rc,rd->rcd", e1x, e1x) + np.einsum("rc,rd->rcd", e2x, e2x)
print(f"  transverse projector  e1e1^T+e2e2^T    : {np.abs(Pi_std-Pi_rnd).max():.2e}")

# tangential trace too (uses normals)
Xb = fibonacci_sphere(N) * 4.0
Nn = normalize(Xb)
Xn = np.concatenate([Xb, Nn], axis=1)
Tt_std = tangential_features(Xn, kdirs, e1, e2, k)
Tt_rnd = tangential_features(Xn, kdirs, e1x, e2x, k)
Gt_std = Tt_std.conj().T @ Tt_std
Gt_rnd = Tt_rnd.conj().T @ Tt_rnd
print(f"  tangential kernel Gram rel diff        : {np.abs(Gt_std-Gt_rnd).max()/np.abs(Gt_std).max():.2e}")

# and the weight-space precision spectrum (eigs of Phi Phi^H) must be basis-invariant
ev_std = np.linalg.eigvalsh(Tt_std @ Tt_std.conj().T)[::-1]
ev_rnd = np.linalg.eigvalsh(Tt_rnd @ Tt_rnd.conj().T)[::-1]
print(f"  eig(Phi Phi^H) rel diff (sorted)       : {np.abs(ev_std-ev_rnd).max()/ev_std.max():.2e}")

# ---------------------------------------------------------------------------
print()
print("=" * 70)
print("PAPER-D : cond(A), A = I + Phi Phi^H / sigma_n^2  (tangential, sphere R=4)")
print("=" * 70)
for (n_spectral, n_b) in [(128, 512), (256, 1024)]:
    kd = normalize(fibonacci_sphere(n_spectral))
    a1, a2 = standard_basis(kd)
    Xb = fibonacci_sphere(n_b) * 4.0
    Xn = np.concatenate([Xb, normalize(Xb)], axis=1)
    Phi = tangential_features(Xn, kd, a1, a2, k)          # (F, 3 n_b)
    F = Phi.shape[0]
    lam = np.linalg.eigvalsh(Phi @ Phi.conj().T).real     # eigenvalues of Phi Phi^H
    lam = np.clip(lam, 0, None)
    lmax, lmin = lam.max(), lam[lam > lam.max() * 1e-16].min()
    lmin_true = lam.min()
    print(f"\n  N_s={n_spectral}  F={F}  N_b={n_b}   (3N_b={3*n_b} rows)")
    print(f"    lambda_max(Phi Phi^H) = {lmax:.3e}")
    print(f"    lambda_min(Phi Phi^H) = {lmin_true:.3e}   (smallest > 1e-16 rel: {lmin:.3e})")
    print(f"    cond(Phi Phi^H) = lam_max/lam_min = {lmax/lmin:.3e}")
    print(f"    sqrt(lam_min) ~ crossover sigma_n = {np.sqrt(lmin):.3e}")
    print(f"    {'sigma_n^2':>12} {'cond(A) exact':>16} {'1/sig^2 model':>16} {'regime':>12}")
    for s2 in [1e0, 1e-3, 6.1e-6, 1e-8, 1e-12, 1e-16]:
        condA = (1 + lmax / s2) / (1 + lmin / s2)
        model = lmax / s2   # naive 1/sigma^2 heuristic (unnormalised)
        if s2 > lmax:
            reg = "cond~1"
        elif s2 > lmin:
            reg = "~lmax/s2"
        else:
            reg = "saturated"
        print(f"    {s2:>12.1e} {condA:>16.3e} {model:>16.3e} {reg:>12}")
    print(f"    thesis default sigma_n^2 = e^-12 = {np.exp(-12):.3e}")
    print(f"    saturation floor cond(A->0) = cond(Phi Phi^H) = {lmax/lmin:.3e}")
