# Review Checklist

How to check an existing tracker row against the paper it came from, column
by column. The goal is to catch real errors and material omissions, not to
rewrite work that is already correct. A row that checks out gets no
suggestions.

Read the shared lens first:
`../lit-review-extractor/references/paper_context.md` (the section's specific
claim, the three community values, the sub-theme examples) and
`../lit-review-extractor/references/column_style_guide.md` (length targets).

## Caps are guidance here, not limits

The extractor treated the per-column word counts as hard ceilings. For review
they are targets: prefer tight wording, but if an important point is missing
and cannot fit under the target, a suggested field **may** exceed it. Never
drop a materially important point just to stay under a count. Do not pad a
field toward its cap either; shorter and precise still wins.

## The two failure modes you are looking for

1. **Inaccuracy** the field says something the paper does not support, or a
   bibliographic value (year, DOI, author, journal, page) is wrong.
2. **Material omission** the field leaves out something that changes how the
   paper reads against the section claim or the three community values. An
   omission is only worth flagging if adding it would change a reader's
   understanding, not merely their word choice. Stylistic preferences are not
   omissions.

## Verbatim-quote check (Quotable moment)

This is the highest-value check. Procedure:

1. Read the cited page number in the existing `Quotable moment`.
2. In the extracted text, find the `===== PAGE N =====` marker for that page.
3. Confirm the quoted words appear there **character for character**
   (ignoring line-break hyphenation the extractor introduced).
4. If the words are present but on a **different** page, suggest the corrected
   page number, keeping the quote.
5. If the words do not appear verbatim anywhere, suggest a replacement quote
   that does appear, with its correct page, and say so in `why`.
6. If nothing quotable supports the row's point, say that plainly in `why`
   rather than inventing a quote.

A paraphrase dressed as a quote, or a page cite that does not hold, is a
correction every time.

## Per-column criteria

- **Paper Title** copy exactly as printed on the paper. Flag a mismatch that
  would break title-based matching.
- **Author(s)** first author's last name; `Last` alone for a sole author,
  `Last et al.` for two or more. No invented co-authors, no initials.
- **Year / Journal or Proceedings / DOI or URL** must match the PDF. If a
  value is not present in the PDF, the correct value is `Not found`; do not
  guess. A guessed DOI is a correction to `Not found`.
- **Sub-theme** 2 to 5 words. Suggest a change only if the label
  misrepresents the paper; a merely different-but-valid label is not worth a
  suggestion.
- **Central claim** must be what the paper actually argues, in the paper's own
  terms. Check it against the abstract and conclusion. Flag drift,
  overstatement, or a claim the paper does not actually make.
- **Key concepts or framework** the paper's own vocabulary, each defined in
  about half a sentence. Flag a concept misattributed to the paper or a
  definition that misstates it.
- **Who is centered** whose perspective the method and framing foreground.
  Flag if the row names the wrong population (e.g. says residents when the
  study interviewed only officials).
- **Value foreclosed** which of equitable access / relational trust /
  flexibility for variable need the framing leaves out, named explicitly, or
  `None directly foreclosed`. Flag a value claimed as foreclosed that the
  paper actually addresses, or a clear foreclosure the row missed.
- **Relevance to argument** the load-bearing column. Check it against the
  section's specific claim (uneven distribution half, infrastructure-without-
  participation half, or both). Apply the **overstated-fit test** below.
- **Gap or limitation** what the paper does not address that the argument
  needs. Flag a limitation that is wrong or a significant one the row omitted
  (for a paywalled paper, the honest "only abstract/intro was accessible"
  caveat is itself a legitimate limitation and should be present).
- **Synthesis paragraph** the 2 to 3 sentence takeaway. Flag it only if it
  repeats Central claim verbatim, contradicts the corrected fields, or
  overstates the fit.

## Overstated-fit test (Relevance to argument)

For papers whose connection to the section claim is thin or indirect, the
style guide requires the row to **say so plainly** rather than force a
strong-sounding sentence. When reviewing:

- If the paper only weakly supports the claim but the row asserts a strong,
  direct fit, that is an overstatement, suggest wording that names the
  thinner or more indirect connection honestly.
- If the row already hedges appropriately ("a thinner fit", "supports the
  broader project rather than this section's claim directly"), leave it.
- Do not swing the other way and understate a genuinely strong, direct fit.

## When a paywalled or preview-only paper was extracted

Several existing rows note that only the abstract, highlights, and
introduction were accessible. On review you will hit the same wall. Do not
treat missing full text as an error in the row. Confirm the caveat is present
and accurate; if the row cites a specific finding from a section that was not
actually accessible, flag that the citation cannot be verified from the
available text.
