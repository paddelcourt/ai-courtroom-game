import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Courtroom Game",
  description: "A courtroom defense game with AI-driven dialogue.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
