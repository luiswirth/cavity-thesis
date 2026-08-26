#import "@local/dottyp:0.1.0": *
#import "@local/dottyp:0.1.0": aliases
#import aliases: *

#let math-template(doc) = {
  show math.equation: set text(font: "New Computer Modern Math")

  set math.mat(delim: "[")
  set math.vec(delim: "[")

  set math.equation(numbering: "(1)")

  // Make equation referencing only display the number, e.g. (3).
  show ref: it => {
    let el = it.element
    if el != none and el.func() == math.equation {
      // Override equation references.
      link(el.location(), numbering(
        el.numbering,
        ..counter(math.equation).at(el.location())
      ))
    } else {
      // Other references as usual.
      it
    }
  }

  doc
}

// Render a CSV scientific-notation string "a.bce-0d" as $a.bc times 10^(-d)$.
#let sci(s) = {
  let parts = s.split("e")
  let mant = calc.round(float(parts.at(0)), digits: 2)
  let exp = int(parts.at(1).trim("+"))
  $#mant times 10^#exp$
}
