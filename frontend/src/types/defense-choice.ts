export type DefenseChoice = {
  id: string;
  testimony_statement_id: string;
  text: string;
  is_correct: boolean;
  feedback: string | null;
  prosecutor_response: string | null;
  judge_response: string | null;
};
