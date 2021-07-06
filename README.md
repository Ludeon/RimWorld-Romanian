A Romanian translation for RimWorld.

See this page for license info:

http://ludeon.com/forums/index.php?topic=2933.0

# Current status

The last "structural update" (step 18. from Tynan's guide): `1.2.3005`

There's still a lot to be translated. Check the issues tab.

## Translation progress statistics

Check the GitHub action tab. Inspect the output of the latest ["Translation stats"](https://github.com/Ludeon/RimWorld-Romanian/actions/workflows/translation_stats.yml) job.

Alternatively, run locally the following python script:
```python
python scripts/t_stats.py -i .
```

# General Notes

- Each XML entry has a comment above containing the English translation. You might want to have the [French translation](https://github.com/Ludeon/RimWorld-fr) opened in a separate tab when translating, for reference.
- XML entries containing the `TODO` string are ignored by the game (the English default will be shown instead).
- XML entries having the comment `<!-- UNUSED -->` above are outdated translations from a previous version of the game, kept as a reference. They should be integrated in the newer tags, or outright deleted altogether.
- Romanian has gendered nouns. Some tags admit a female version (e.g. `<title>` and `<titleFemale>` in `Backstories.xml`). Cross-check the [French translation](https://github.com/Ludeon/RimWorld-fr) for inspiration.
- [DeepL](https://www.deepl.com/translator) is a great tool to speed up the translation, especially for long bodies of text. Don't just copy and paste, proofread what is translated and correct if necessary.

## Choices of some translations
This table is for keeping consistent translations of certain words.

|EN word|Chosen translation|
|-|-|
|dumping stockpile|haldă|
|dumping area|zona de haldă|
|stockpile|zonă de depozitare|
|(mining) skill|aptitudine|
|skilled at ...|e îndemânat la ...|
|melee|corp la corp|
|slaughter|măcelărește|
|skip, farskip|teleportare|
|(map) tile|țiglă|
|map|hartă|
|mental break|cădere nervoasă|
|mentally broken|afectat mental|
|lavish (meal)|somptuos|
|mood|dispoziție|
|blight|molimă|
|blunt| ? |

|Not to be translated|
|-|
|Cooldown|Cooldown|
|Psyfocus|Psyfocus|
|hitpoints|hitpoint-uri|