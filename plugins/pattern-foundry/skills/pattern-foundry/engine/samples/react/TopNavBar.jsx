import React from 'react';
import { motion } from 'framer-motion';
import PrimaryButton from './PrimaryButton';

/**
 * TopNavBar — Brand-neutral sticky navigation
 *
 * Extracted system patterns (manually verified source site):
 *   outer:  max-width 1440px, height 82px (confirmed .lp_ed_navbar)
 *   inner:  1296px wrapper (confirmed .lp_nav_wrapper)
 *   scroll: shadow appears on scroll (nav.scrolled class)
 *   mobile: primary CTA only — links hidden below lg breakpoint
 *
 * Adapt: replace [YourBrand] and navLinks with your product's navigation.
 */
const TopNavBar = () => {
  const navLinks = [
    { name: '[Category One]', href: '#' },
    { name: '[Category Two]', href: '#' },
    { name: '[Features]',     href: '#' },
    { name: '[Pricing]',      href: '#' },
  ];

  return (
    <nav
      className="w-full h-[82px] bg-white border-b border-[#eff4f7] sticky top-0 z-[1000] flex items-center shadow-[rgba(125,125,125,0.15)_0px_1px_4px]"
      aria-label="Primary navigation"
    >
      <div className="max-w-[1296px] w-full mx-auto px-4 flex items-center justify-between">

        {/* Logo + nav links */}
        <div className="flex items-center gap-10">
          <a href="/" className="font-black text-[#193f68] text-xl tracking-tight">
            [YourBrand]
          </a>

          {/* Desktop links */}
          <div className="hidden lg:flex items-center gap-6">
            {navLinks.map(link => (
              <a
                key={link.name}
                href={link.href}
                className="text-[15px] font-medium text-[#4b5661] hover:text-[var(--color-action,#fe6724)] transition-colors duration-200"
              >
                {link.name}
              </a>
            ))}
          </div>
        </div>

        {/* Auth actions */}
        <div className="flex items-center gap-3">
          <a href="#" className="hidden sm:block text-[15px] font-bold text-[#86949d] hover:text-[#111111] px-3 py-2 transition-colors">
            Log in
          </a>
          <PrimaryButton variant="action" className="h-[40px] px-5 text-sm">
            Start for Free
          </PrimaryButton>
        </div>
      </div>
    </nav>
  );
};

export default TopNavBar;
