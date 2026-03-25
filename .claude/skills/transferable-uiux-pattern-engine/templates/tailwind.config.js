/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          orange: '#fe6724',
          navy: '#193f68',
          gold: '#f0b400',
        },
        surface: {
          light: '#ffffff',
          alt: '#e9f1fc',
          pale: '#eff4f7',
          hover: '#f6fcff',
        },
        text: {
          primary: '#111111',
          secondary: '#4b5661',
          muted: '#86949d',
          dark: '#010b24',
        },
        accent: {
          blue: '#1a73e8', // Login only
          info: '#a6d8fa',
        }
      },
      fontFamily: {
        sans: ['Lato', 'Inter', 'sans-serif'],
        serif: ['Georgia', 'serif'],
      },
      fontSize: {
        'xs': '11px',
        'sm': '13px',
        'base': '16px',
        'lg': '18px',
        'xl': '20px',
        '2xl': '24px',
        'hero': '42px',
      },
      fontWeight: {
        normal: 400,
        bold: 700,
        black: 900,
      },
      borderRadius: {
        'sm': '5px',
        'md': '8px',
        'lg': '20px',
        'xl': '32px',
        'full': '50%',
      },
      boxShadow: {
        'default': '0px 4px 12px rgba(0,0,0,0.08)',
        'hover': '0px 10px 30px rgba(0,0,0,0.12)',
        'ambient': '1px 1px 60px 40px rgba(229,229,229,0.25)',
      },
      transitionDuration: {
        'fast': '200ms',
        'standard': '300ms',
        'slow': '450ms',
      },
      transitionTimingFunction: {
        'standard': 'cubic-bezier(0.4, 0, 0.2, 1)',
      },
      backgroundImage: {
        'feature-gradient': 'linear-gradient(135deg, #ff9a1f 0%, #f97316 100%)',
      },
      spacing: {
        'section': '128px',
      },
      maxWidth: {
        'nav': '1440px',
        'content': '1296px',
        'footer': '1100px',
        'hero-left': '550px',
      }
    },
  },
  plugins: [],
}
