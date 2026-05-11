import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// `base` is overridable through VITE_BASE so the same code can serve from
// `/` (local dev / preview), `/gonzomlpodcastsurvey/` (GitHub Pages under the
// default repo name), or any custom domain root.
export default defineConfig(({ command }) => ({
  base:
    process.env.VITE_BASE ??
    (command === "build" ? "/gonzomlpodcastsurvey/" : "/"),
  plugins: [react()],
  server: { port: 5174, open: true },
}));
