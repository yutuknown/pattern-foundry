import React from 'react';
import TopNavBar  from './TopNavBar';
import MainHero   from './MainHero';
import FeatureCard from './FeatureCard';
import SiteFooter  from './SiteFooter';

/**
 * App — Brand-neutral page assembly example
 *
 * Demonstrates the extracted design system applied to a generic page.
 * All [PLACEHOLDER] text must be replaced with your brand content.
 * All token values (colors, spacing) can be overridden via CSS custom properties.
 *
 * Extracted system patterns used:
 *   - Navbar: 82px height, 1296px inner
 *   - Hero: 128px section padding, 550px text column
 *   - Feature grid: 3-col, gradient cards (radius 20px), hover lift
 *   - Content section: white bg, 128px padding, 1296px container
 *   - CTA section: authority bg (#193f68), centered, white text
 *   - Footer: surface bg (#e9f1fc), 1100px inner
 */
const App = () => {
  const features = [
    {
      icon: '📋',
      title: '[Feature One]',
      desc: '[1-sentence benefit. Active verb + outcome.]',
    },
    {
      icon: '🃏',
      title: '[Feature Two]',
      desc: '[1-sentence benefit. Active verb + outcome.]',
    },
    {
      icon: '📈',
      title: '[Feature Three]',
      desc: '[1-sentence benefit. Active verb + outcome.]',
    },
  ];

  return (
    <div className="min-h-screen font-sans text-[#111111] bg-white antialiased">

      {/* Skip to content — accessibility required */}
      <a
        href="#main-content"
        className="sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-50 focus:bg-white focus:px-4 focus:py-2 focus:rounded focus:shadow-lg focus:text-[#193f68] focus:font-bold"
      >
        Skip to main content
      </a>

      <TopNavBar />

      <main id="main-content">
        <MainHero />

        {/* Feature grid section */}
        <section className="bg-[#eff4f7] py-[128px]" aria-labelledby="features-heading">
          <div className="max-w-[1296px] mx-auto px-4">
            <h2 id="features-heading" className="text-[42px] font-black text-center mb-4 text-[#010b24]">
              [Section heading — "Everything you need to [outcome]"]
            </h2>
            <p className="text-center text-[#4b5661] text-lg mb-14 max-w-[55ch] mx-auto">
              [Section subheadline — 1 sentence elaboration]
            </p>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {features.map(f => (
                <FeatureCard key={f.title} variant="feature">
                  <div className="text-4xl mb-4">{f.icon}</div>
                  <h3 className="text-xl font-bold mb-2">{f.title}</h3>
                  <p className="text-white/90 text-sm">{f.desc}</p>
                </FeatureCard>
              ))}
            </div>
          </div>
        </section>

        {/* Content cards section */}
        <section className="bg-white py-[128px]" aria-labelledby="content-heading">
          <div className="max-w-[1296px] mx-auto px-4">
            <h2 id="content-heading" className="text-[42px] font-black mb-12 text-[#010b24]">
              [Browse / Explore heading]
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
              {[1, 2, 3, 4].map(i => (
                <FeatureCard key={i} variant="course" className="p-0 flex flex-col">
                  <div className="aspect-[16/10] bg-[#e9f1fc] flex items-center justify-center text-[#86949d] text-sm">
                    [Visual]
                  </div>
                  <div className="p-5">
                    <div className="text-xs font-bold text-[var(--color-action,#fe6724)] uppercase mb-2">
                      [Category]
                    </div>
                    <h3 className="text-base font-bold text-[#111111] mb-1 leading-snug">
                      [Content item title {i}]
                    </h3>
                    <div className="mt-3 flex items-center justify-between text-xs text-[#86949d]">
                      <span>[N]+ enrolled</span>
                      <span className="text-[#f0b400] font-bold">4.9 ★</span>
                    </div>
                  </div>
                </FeatureCard>
              ))}
            </div>
          </div>
        </section>

        {/* Mid-page CTA section */}
        <section className="bg-[#193f68] py-24 text-white" aria-labelledby="cta-heading">
          <div className="max-w-[1296px] mx-auto px-4 text-center">
            <p className="text-base text-white/70 mb-3">[N]+ people already [doing the thing]</p>
            <h2 id="cta-heading" className="text-[42px] font-black text-white mb-6">
              [CTA section headline — "Start [outcome] for Free"]
            </h2>
            <p className="text-white/80 text-lg mb-10 max-w-[44ch] mx-auto">
              [Supporting line — risk-reducer or social proof]
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <button className="bg-[var(--color-action,#fe6724)] text-white px-8 py-3 rounded-[8px] font-bold text-base hover:opacity-90 transition-opacity">
                Start for Free
              </button>
              <button className="bg-white/10 border border-white/20 text-white px-8 py-3 rounded-[8px] font-bold text-base hover:bg-white/20 transition-colors">
                [Secondary CTA]
              </button>
            </div>
            <p className="mt-5 text-white/50 text-xs">No credit card · Cancel anytime</p>
          </div>
        </section>
      </main>

      <SiteFooter />
    </div>
  );
};

export default App;
