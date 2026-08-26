#import "@local/dottyp:0.1.0": *
#import "@local/dottyp:0.1.0": aliases
#import aliases: *

// Sans text with the serif math face, which is how this thesis has always been
// set: dottyp's sans set pairs sans text with sans math.
#let thesis-fonts = (
  text: "New Computer Modern Sans",
  math: "New Computer Modern Math",
)

// Render a CSV scientific-notation string "a.bce-0d" as $a.bc times 10^(-d)$.
#let sci(s) = {
  let parts = s.split("e")
  let mant = calc.round(float(parts.at(0)), digits: 2)
  let exp = int(parts.at(1).trim("+"))
  $#mant times 10^#exp$
}
