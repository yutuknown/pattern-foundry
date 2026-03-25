import React from 'react';
import { motion } from 'framer-motion';
import PrimaryButton from './PrimaryButton';

/**
 * MainHero — Brand-neutral hero section
 *
 * Extracted system patterns (manually verified source site):
 *   section padding:   128px 0 (confirmed .er-crse-wrap / hero-related)
 *   hero left column:  max-width 550px (confirmed .hero-left-container)
 *   SEO h1 pattern:    small (18px/700) for crawlers, large h2 (42px/900) for humans
 *   section container: max-width 1296px
 *   hero bg pattern:   white or dark navy gradient
 *
 * Adapt:
 *   - Replace [SEO_TITLE], [VISUAL_HEADLINE], [SUBHEADLINE] with your copy.
 *   - Replace trust badge text with your own proof signal.
 *   - Swap gradient/bg to your brand's hero background.
 */
const MainHero = () => {
  return (
    <section className="bg-white py-[128px]">
      <div className="max-w-[1296px] mx-auto px-4 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">

        {/* Text column — constrained to 550px */}
        <div className="max-w-[550px]">

          {/* Trust badge / eyebrow */}
          <motion.div
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            className="inline-flex items-center gap-2 text-xs font-bold bg-[#e9f1fc] text-[#193f68] px-3 py-1.5 rounded-full mb-5 border border-[#a6d8fa]/60"
          >
            [Trust signal — e.g., "Backed by Y Combinator" or "4.8★ rating"]
          </motion.div>

          {/* SEO H1 — small, keyword-rich, for crawlers */}
          <h1 className="text-[18px] font-bold text-[#193f68] mb-3 tracking-tight">
            [SEO_TITLE — keyword-rich, 1 sentence]
          </h1>

          {/* Visual H2 — the real human-facing hero headline */}
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1, duration: 0.45, ease: [0.4, 0, 0.2, 1] }}
            className="text-[42px] font-black text-[#111111] leading-tight mb-6"
            aria-hidden="true"
          >
            [VISUAL_HEADLINE — outcome-first, ≤10 words, sentence case]
          </motion.p>

          <p className="text-[#4b5661] text-[18px] mb-8 leading-relaxed max-w-[44ch]">
            [SUBHEADLINE — platform mechanism + who it's for, 1-2 sentences]
          </p>

          {/* CTA group */}
          <div className="flex flex-wrap gap-3">
            <PrimaryButton variant="action" className="h-[48px] px-7 text-base">
              Start [Action] for Free
            </PrimaryButton>
            <PrimaryButton variant="oauth" className="h-[48px] px-7 text-base gap-3">
              Continue with Google
            </PrimaryButton>
          </div>

          {/* Social proof micro */}
          <p className="mt-5 text-xs text-[#86949d]">
            ⭐ [X.X] rating &nbsp;·&nbsp; [N]+ [users] already using it
          </p>
        </div>

        {/* Visual column */}
        <motion.div
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.3, duration: 0.6 }}
          className="relative rounded-[32px] overflow-hidden bg-[#eff4f7] aspect-[4/3] flex items-center justify-center text-[#86949d] italic"
          aria-hidden="true"
        >
          {/* Replace with your hero image or product screenshot */}
          [Hero visual — product screenshot or illustration]
        </motion.div>
      </div>
    </section>
  );
};

export default MainHero;
