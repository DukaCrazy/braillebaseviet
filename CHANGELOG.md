
## 2026/9/6 - Version 0.2.9 Sumary
- Update to the logic that processes uppercase and lowercase characters.

## 2026/09/03 - Version 0.2.8 Summary
- Implementation of the tonal braille system in the Vietnamese BrailleBase dictionary.
- Significant improvement in translation accuracy, especially for accented vowels and complex tonal combinations.
- Expanded braille mapping coverage to reflect modern Vietnamese orthographic rules.
- Internal adjustments to the tokenization module to support tonal composition without information loss.
## 2026/08/31 - Version 0.2.7 Summary
- braillebase 0.2.7
## 2026/08/11 - Version 0.1.6 Summary
### Added
- Full implementation of the BrailleBaseOutput module, responsible for generating multiple output formats based on the data processed by braillebase.
### New export methods:
- output_all_json — detailed JSON structure generation.
- output_all_csv — tabular CSV export.
- output_all_xml — formatted and validated XML output.
- output_all_yaml — clean and readable YAML output.
- output_all_markdown — Markdown documentation with organized sections.
- output_all_html — HTML rendering with tables and a standardized layout.
- output_all_txt — plain text output, ideal for logs and quick inspection.
### Improved
- Complete separation of heavy formatting logic, removing duplication and reducing coupling with the main module.
- Standardization of output fields (index, braille, binary, numbering, unicode, reverse).
- Ensured consistency across all formats, including cross‑validation of Unicode and reverse braille cells.
- Enhanced readability of all outputs with consistent indentation and clear data organization.

## 2026/08/11 - Version 0.1.5 Summary
- BrailleBase: Adjustments to the token size definition caused a bug that was not detected in the testing environment but was noticed after the version was released. The inconsistency has been fixed.

## 2026/08/02 - Version 0.1.4 Summary
- braillebase 0.1.4

## 2026/08/01 - Version 0.1.3 Summary
- Table update, addition of new characters, and improved alignment with the UEB standard.


<img src="./img/logo.png" alt="Logo" width="500" height="493">
