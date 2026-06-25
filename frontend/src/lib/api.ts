import type { CaseFile } from "@/types/case";

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000/api/v1";

export async function getCases(): Promise<CaseFile[]> {
  try {
    const response = await fetch(`${API_URL}/cases`, {
      next: { revalidate: 10 },
    });

    if (!response.ok) {
      return [];
    }

    return response.json();
  } catch {
    return [];
  }
}
