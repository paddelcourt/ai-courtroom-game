"use client";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { useRef, useState } from "react";
import { generateCase, getCaseEvidence, getCaseTestimony, getTestimonyChoices, getCharacter } from "@/lib/api";
import type { CaseFile } from "@/types/case";
import type { Evidence } from "@/types/evidence";
import type { DefenseChoice } from "@/types/defense-choice";
import type { TestimonyStatement } from "@/types/testimony";
import type { Character } from "@/types/character";


export default function Home() {
  const [theme, setTheme] = useState("museum theft")
  const [caseFile, setCaseFile] = useState<CaseFile | null>(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [isMusicPlaying, setIsMusicPlaying] = useState(false);
  const [volume, setVolume] = useState(0.4);
  const [evidence, setEvidence] = useState<Evidence[]>([]);
  const [testimony, setTestimony] = useState<TestimonyStatement[]>([]);
  const [currentTestimonyIndex, setCurrentTestimonyIndex] = useState(0);
  const [choices, setChoices] = useState<DefenseChoice[]>([]);
  const [selectedChoice, setSelectedChoice] = useState<DefenseChoice | null>(null);
  const [correctCount, setCorrectCount] = useState(0);
  const [currentCharacter, setCurrentCharacter] = useState<Character | null>(null);
  const isFinished = testimony.length > 0 && currentTestimonyIndex >= testimony.length;
  const wonTrial = isFinished && correctCount === testimony.length;
  const [isMusicPanelOpen, setIsMusicPanelOpen] = useState(false);
  const currentTestimony = testimony[currentTestimonyIndex] ?? null;

  async function handleGenerateCase() {
    setCurrentTestimonyIndex(0);
    setIsLoading(true);
    setError(null)

    try {
      const generatedCase = await generateCase(theme);
      const caseEvidence = await getCaseEvidence(generatedCase.id)
      const caseTestimony = await getCaseTestimony(generatedCase.id)
      if (caseTestimony[0]){
        const defenseChoices = await getTestimonyChoices(caseTestimony[0].id)
        setChoices(defenseChoices)
        const character = await getCharacter(caseTestimony[0].character_id);
        setCurrentCharacter(character);
        

      }
      setCaseFile(generatedCase);
      setEvidence(caseEvidence);
      setTestimony(caseTestimony);
      if (audioRef.current) {
        audioRef.current.volume = volume;
        await audioRef.current.play();
        setIsMusicPlaying(true);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong")
      setIsMusicPlaying(false);
    }
    finally {
      setIsLoading(false)
    }
  }


  function handleVolumeChange(event: React.ChangeEvent<HTMLInputElement>) {
    const nextVolume = Number(event.target.value);
    setVolume(nextVolume);
    if (audioRef.current) {
      audioRef.current.volume = nextVolume;
    }
  }

  async function handleToggleMusic() {
    const audio = audioRef.current;
    if (!audio) return;

      if (audio.paused) {
        audio.volume = volume;
        await audio.play();
        setIsMusicPlaying(true);
      } else {
        audio.pause();
        setIsMusicPlaying(false);
      }
    }

    async function handleSelectChoice(choice: DefenseChoice) {
      if (selectedChoice) return;

        const sound = new Audio("/audio/objection-sound-effect.mp3");
        sound.volume = 0.35;
        sound.play();
        if (audioRef.current) {
          audioRef.current.src = "/audio/objection-theme.mp3";
          audioRef.current.currentTime = 0;
          audioRef.current.play().catch(() => {});
          setIsMusicPlaying(true);
        }

        setSelectedChoice(choice);

      if (choice.is_correct) {
      setCorrectCount((count) => count + 1);
    }
    }

    async function handleNextTestimony() {
      const nextIndex = currentTestimonyIndex + 1;
      const nextTestimony = testimony[nextIndex]
      setSelectedChoice(null);
      setCurrentTestimonyIndex(nextIndex)

      if (nextTestimony) {
        const nextChoices = await getTestimonyChoices(nextTestimony.id)
        setChoices(nextChoices)

        const character = await getCharacter(nextTestimony.character_id);
        setCurrentCharacter(character);
      }

      else {
        setChoices([]);
        setCurrentCharacter(null);
      }
    }



  return (
    <main className="mx-auto flex min-h-screen w-full max-w-5xl flex-col gap-6 px-4 py-6 sm:px-6 lg:px-8">
      <audio ref={audioRef} src="/audio/courtroom-theme.mp3" loop />
      <Card>
        <CardHeader>
          <CardTitle className="text-3xl">Ace Attorney Simulator</CardTitle>
          <CardDescription>
            Generate a courtroom scenario in a style similar to Phoenix Wright game.
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex flex-col gap-3 sm:flex-row">
            <Input
              aria-label="Case theme"
              value={theme}
              onChange={(event) => setTheme(event.target.value)}
            />
            <Button onClick={handleGenerateCase} disabled={isLoading}>
            {isLoading ? "Generating..." : "Generate Case"}
          </Button>
          </div>

        {error ? <p className="text-sm text-red-500">{error}</p> : null}

        {caseFile ? (
            <div className="rounded-md border p-4">
              <h2><b>{caseFile.title}</b></h2>
              <p>{caseFile.description}</p>
            </div>
          ) : null}
        {caseFile ? (
            <div className="fixed bottom-4 right-4 z-50 rounded-md border bg-card p-3 shadow-lg">
              <Button
                size="sm"
                variant="secondary"
                onClick={() => setIsMusicPanelOpen((open) => !open)}
              >
                {isMusicPanelOpen ? "Hide music" : "Music"}
              </Button>

              {isMusicPanelOpen ? (
                <div className="mt-3 w-64">
                  <div className="mb-3 flex items-center justify-between gap-3">
                    <span className="text-sm font-medium">Music</span>
                    <Button size="sm" variant="secondary" onClick={handleToggleMusic}>
                      {isMusicPlaying ? "Pause" : "Play"}
                    </Button>
                  </div>

                  <label className="block text-xs text-muted-foreground" htmlFor="music-volume">
                    Volume
                  </label>
                  <input
                    id="music-volume"
                    className="mt-2 w-full"
                    type="range"
                    min="0"
                    max="1"
                    step="0.05"
                    value={volume}
                    onChange={handleVolumeChange}
                  />
                </div>
              ) : null}
            </div>
          ) : null}
        </CardContent>
      </Card>

      {currentTestimony ? (
  <Card>
    <CardHeader>
      <CardTitle>Testimony {currentTestimony.order_index}</CardTitle>
      <p>As a defense attorney, select a defense choice based on the testimony and evidence below</p>
    </CardHeader>

    <CardContent className="space-y-4">
      <div className="rounded-md border bg-background p-4">
        <p className="text-base leading-7">{currentCharacter?.name}</p>
        <p className="text-base leading-7">{currentTestimony.text}</p>
      </div>

      <div className="space-y-3">
        {choices.map((choice) => (
          <Button
          variant="outline"
            key={choice.id}
            onClick={() => handleSelectChoice(choice)}
            disabled={selectedChoice !== null}
            className="h-auto w-full justify-start whitespace-normal px-4 py-3 text-left leading-6"
          >
            {choice.text}
          </Button>
        ))}
        {selectedChoice ? (
        <div className="rounded-md border p-4">
          <p className="font-semibold">
            {selectedChoice.is_correct ? "Correct" : "Incorrect"}
          </p>

          <p className="mt-2 text-sm">
            {selectedChoice.feedback}
          </p>

          <div className="mt-4 space-y-2 text-sm">
            <p>
              <span className="font-semibold">Prosecutor:</span>{" "}
              {selectedChoice.prosecutor_response}
            </p>

            <p>
              <span className="font-semibold">Judge:</span>{" "}
              {selectedChoice.judge_response}
            </p>
          </div>
        </div>
      ) : null}
        {selectedChoice ? (
            <Button onClick={handleNextTestimony}>
              {currentTestimonyIndex + 1 >= testimony.length
                ? "Finish Trial"
                : "Next Testimony"}
            </Button>
          ) : null}
      </div>
    </CardContent>
  </Card>
) : null}

      
    {evidence.length > 0 ? (
            <div className="rounded-md border p-4">
              <h3 className="font-semibold">Evidence</h3>
              <div className="mt-3 space-y-3">
                {evidence.map((item) => (
                  <div key={item.id} className="rounded-md border p-3">
                    <p className="font-medium">{item.name}</p>
                    <p className="text-sm text-muted-foreground">{item.description}</p>
                  </div>
                ))}
              </div>
            </div>
          ) : null}

    {isFinished ? (
    <Card>
      <CardHeader>
        <CardTitle>{wonTrial ? "Not Guilty" : "Guilty"}</CardTitle>
        <CardDescription>
          {wonTrial
            ? "You successfully defended your client."
            : "The defense failed to resolve every contradiction."}
        </CardDescription>
      </CardHeader>
      <CardContent>
        <p className="text-sm text-muted-foreground">
          You found {correctCount} out of {testimony.length} contradictions.
        </p>
      </CardContent>
    </Card>
  ) : null}
    </main>
  );
}
