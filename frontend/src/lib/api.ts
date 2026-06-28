import type { CaseFile } from "@/types/case";
import { DefenseChoice } from "@/types/defense-choice";
import type { Evidence } from "@/types/evidence";
import type { TestimonyStatement } from "@/types/testimony";
import type { Character } from "@/types/character";

export const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000/api/v1";


export async function generateCase(theme: string): Promise<CaseFile> {
    const params = new URLSearchParams({ theme });

    const response = await fetch(`${API_URL}/cases/generate?${params.toString()}`, {
    method: "POST",
  });

  if (!response.ok) {
    throw new Error("Failed to generate case")
  }

  return response.json()
}


export async function getCaseEvidence(caseId: string): Promise<Evidence[]> {
    const response = await fetch(`${API_URL}/cases/${caseId}/evidence`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch evidence")
  }

  return response.json()
}


export async function getCaseTestimony(caseId: string): Promise<TestimonyStatement[]> {
    const response = await fetch(`${API_URL}/cases/${caseId}/testimony`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch testimony")
  }

  return response.json()
}

export async function getTestimonyChoices(testimonyId: string): Promise<DefenseChoice[]> {
    const response = await fetch(`${API_URL}/testimony/${testimonyId}/choices`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch choices")
  }

  return response.json()
}

export async function getCharacter(characterId: string): Promise<Character> {
    const response = await fetch(`${API_URL}/characters/${characterId}`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch choices")
  }

  return response.json()
}

