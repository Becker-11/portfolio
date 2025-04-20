// frontend/src/app/layout.tsx
import './globals.css';

// app/layout.tsx
import React from 'react';
import { ReactNode } from 'react';

const Layout = ({ children }: { children: ReactNode }) => {
  return (
    <html lang="en">
      <head>
        <title>AI Safety Research</title>
        {/* Other meta tags can go here */}
      </head>
      <body>
        <header>
          <h1>Welcome to AI Safety Research</h1>
          {/* Add navigation or any global layout elements here */}
        </header>
        <main>{children}</main>
      </body>
    </html>
  )
}

export default Layout
