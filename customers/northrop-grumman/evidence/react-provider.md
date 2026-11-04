# React Provider

Source: `src/index.tsx`. Working-tree snapshot on 2026-11-04; original line numbers retained.

## Lines 1 to 28

```text
1: import React from "react";
2: import { createRoot } from "react-dom/client";
3: import "./styles/index.css";
4: import App from "./App";
5: import { SisenseContextProvider } from "@sisense/sdk-ui";
6: import { ThemeModeProvider } from "./theme/themeMode";
7:
8: const container = document.getElementById("root");
9: if (container) {
10:   const root = createRoot(container);
11:   root.render(
12:     <React.StrictMode>
13:       <ThemeModeProvider>
14:         <SisenseContextProvider
15:           url="https://analytics.oneexiger.com"
16:           ssoEnabled={true}
17:           appConfig={{
18:             queryCacheConfig: {
19:               enabled: true,
20:             },
21:           }}
22:         >
23:           <App />
24:         </SisenseContextProvider>
25:       </ThemeModeProvider>
26:     </React.StrictMode>,
27:   );
28: }
```
