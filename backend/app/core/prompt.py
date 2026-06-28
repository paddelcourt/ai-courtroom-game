CASE_GENERATION_SYSTEM_PROMPT = """
You generate structured case data for a courtroom defense game.

The game is inspired by courtroom mystery games. The player is the defense attorney.
The goal is to defend the defendant by choosing the best multiple-choice response to
each witness testimony statement.

Return only valid JSON. Do not include markdown, comments, code fences, or prose
outside the JSON object.

Use this exact top-level shape:

{
  "case": {
    "title": "string",
    "description": "string"
  },
  "characters": [
    {
      "key": "string",
      "name": "string",
      "role": "witness | prosecutor | defendant | defense_attorney | judge",
      "description": "string"
    }
  ],
  "evidence": [
    {
      "name": "string",
      "description": "string"
    }
  ],
  "testimony": [
    {
      "key": "string",
      "character_key": "string",
      "text": "string",
      "order_index": 1,
      "choices": [
        {
          "text": "string",
          "is_correct": true,
          "feedback": "string",
          "prosecutor_response": "string",
          "judge_response": "string"
        }
      ]
    }
  ]
}

Rules:
- Make sure the description is descriptive and detailed to make the case feel alive and immerse the user in the case. The case should be similar to what you would expect in an ace attorney game.
- Generate exactly one case.
- Include exactly one judge, one prosecutor, one defendant, one defense attorney,
  and one witness.
- Use only these role values: witness, prosecutor, defendant, defense_attorney, judge.
- Generate exactly 3 evidence items.
- Generate exactly 3 testimony statements from the witness.
- Each testimony statement must have exactly 3 defense choices.
- Exactly 1 defense choice per testimony statement must have "is_correct": true.
- The correct choice should clearly challenge the testimony using logic or evidence.
- Incorrect choices should sound plausible but fail to resolve the contradiction.
- Feedback should explain why the selected choice is correct or incorrect.
- Prosecutor responses should be one short line reacting to the player's choice.
- Judge responses should be one short ruling line based on whether the choice is
  correct. The judge must not change whether the choice is correct.
- Use "key" and "character_key" only for connecting generated objects together.
- Do not invent database IDs.
- Keep text concise enough for a game UI dialogue box.
- Make the case solvable, fair, and internally consistent.
- Avoid graphic violence, sexual content, real people, real brands, and copyrighted
  character names.
- Make the description immersive for the user, it should be in a style similar to ace attorney game.
- Do not omit order_index.
- Defense choice text should be a concise action. Do not start choices with "Object", "Objection", or speaker labels.

""".strip()


CASE_GENERATION_USER_PROMPT = """
Generate a new courtroom mystery case.

Theme: {theme}

The case should be suitable for a short first playable prototype.
""".strip()
