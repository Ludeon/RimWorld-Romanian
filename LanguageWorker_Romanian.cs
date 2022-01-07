// Verse.LanguageWorker_Romanian
using Verse;

public class LanguageWorker_Romanian : LanguageWorker
{
	public override string WithIndefiniteArticle(string str, Gender gender, bool plural = false, bool name = false)
	{
		if (name)
		{
			return str;
		}
		if (plural)
		{
			if (gender != Gender.Male)
			{
				return str + "e";
			}
			return str + "i";
		}
		return ((gender == Gender.Female) ? "a " : "un ") + str;
	}

	public override string WithDefiniteArticle(string str, Gender gender, bool plural = false, bool name = false)
	{
		if (str.NullOrEmpty())
		{
			return str;
		}
		if (name)
		{
			return str;
		}
		char ch = str[str.Length - 1];
		if (plural)
		{
			if (gender != Gender.Male)
			{
				return str + "e";
			}
			return str + "i";
		}
		if (!IsVowel(ch))
		{
			return str + "ul";
		}
		if (gender == Gender.Male)
		{
			return str + "le";
		}
		return str + "a";
	}

	public bool IsVowel(char ch)
	{
		return "aeiouăâîAEIOUĂÂÎ".IndexOf(ch) >= 0;
	}

/*
    public override string OrdinalNumber(int number, Gender gender = Gender.None) {
        // TODO
    }

    public override string Pluralize(string str, Gender gender, int count = -1) {
        // TODO
    }

    public override string PostProcessed(string str) {
        // TODO
    }
*/
}
