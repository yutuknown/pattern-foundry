import React from 'react';
import { motion } from 'framer-motion';

/**
 * PrimaryButton — Brand-neutral button component
 *
 * Extracted system patterns (manually verified source site):
 *   action:    bg action-color, radius 5-8px  → primary CTAs
 *   authority: bg authority-color             → secondary/trust actions
 *   ghost:     bg #eff4f7, muted text         → low-priority actions
 *   oauth:     bg white, brand border         → third-party auth
 *
 * Adapt: swap color values to your brand tokens.
 */
const PrimaryButton = ({
  children,
  variant = 'action',
  onClick,
  className = '',
}) => {
  const base =
    'px-4 py-2 text-sm font-bold transition-all duration-200 rounded-[5px] flex items-center justify-center';

  const variants = {
    action:    'bg-[var(--color-action,#fe6724)] text-white hover:opacity-90',
    authority: 'bg-[var(--color-authority,#193f68)] text-white hover:opacity-90',
    ghost:     'bg-[#eff4f7] text-[#86949d] hover:bg-[#dce6ed]',
    outline:   'border border-[var(--color-authority,#193f68)] text-[var(--color-authority,#193f68)] hover:bg-[#e9f1fc]',
    oauth:     'bg-white text-[#3c4043] border border-[#dadce0] rounded-[8px] sm:rounded-[60px]',
  };

  return (
    <motion.button
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
      className={`${base} ${variants[variant] ?? variants.action} ${className}`}
      onClick={onClick}
    >
      {children}
    </motion.button>
  );
};

export default PrimaryButton;
