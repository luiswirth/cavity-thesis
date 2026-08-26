#import "setup.typ": *

#title-page(
  logo: image("../res/ethz-logo.svg"),
  kind: "Semester Thesis",
  title: [
    BEM Benchmark of the \
    Ehrenpreis--Palamodov Gaussian Process \
    for Maxwell Cavity Scattering
  ],
  abstract: [
  This thesis presents a high-fidelity benchmark for the Ehrenpreis--Palamodov Gaussian Process (EPGP),
  a probabilistic solver whose plane-wave prior satisfies the time-harmonic Maxwell equations exactly by construction.
  The benchmark is an interior electromagnetic scattering problem in a perfectly electrically conducting cavity,
  where dipole sources on an interior sphere excite a field that is measured back on the same sphere,
  defining a reaction operator from dipole excitations to field responses.
  We reconstruct this operator with the EPGP and compare it against an independent boundary element method (BEM) reference using Bembel #cite(<bembel>).
  We investigate two cavity geometries.
  On the spherical cavity, where the reaction operator is available in closed form,
  both solvers match it to a relative Frobenius-norm error between $10^(-10)$ and $10^(-12)$.
  On the ellipsoidal cavity, which admits no analytic solution,
  the EPGP agrees with the BEM reference to a relative Frobenius-norm error of about $10^(-8)$.
  This establishes the EPGP as an accurate, Maxwell-consistent solver for the interior cavity problem
  and certifies the reaction operator as a robust reference benchmark.
  We further study convergence, the accuracy--runtime trade-off, and uncertainty quantification.
  ],
  author: "Luis Wirth",
  contact: [
    #link("mailto:luwirth@ethz.ch")[luwirth\@ethz.ch] \
    #link("http://ethz.lwirth.com")[ethz.lwirth.com]
  ],
  supervisor: "Prof. Dr.-Ing. Stefan Kurz",
  affiliation: "Seminar for Applied Mathematics",
  date: "1st July 2026",
)
