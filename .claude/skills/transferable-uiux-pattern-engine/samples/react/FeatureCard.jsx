import React from 'react';
import { motion } from 'framer-motion';

/**
 * FeatureCard — Brand-neutral card component
 *
 * Extracted system patterns (manually verified source site):
 *   course:  radius 32px, ambient shadow     → content/listing cards
 *   feature: radius 20px, warm gradient      → product feature highlights
 *   surface: radius 16px, tinted bg          → subtle info cards
 *
 * Physical hover: translateY(-3px) at 0.45s cubic-bezier(0.4, 0, 0.2, 1)
 *
 * Adapt: replace gradient colors with your brand warm palette.
 */
const FeatureCard = ({
  children,
  variant = 'feature',
  className = '',
}) => {
  const base = 'transition-all overflow-hidden';

  const variants = {
    course:  'bg-white rounded-[32px] shadow-[1px_1px_60px_40px_rgba(229,229,229,0.25)] hover:shadow-[0px_10px_30px_rgba(0,0,0,0.12)]',
    feature: 'bg-gradient-to-br from-[#ff9a1f] to-[#f97316] rounded-[20px] text-white p-6 shadow-md hover:shadow-lg',
    surface: 'bg-[#e9f1fc] rounded-[16px] p-4 border border-[#a6d8fa]/50',
  };

  return (
    <motion.div
      whileHover={{ y: -3, transition: { duration: 0.45, ease: [0.4, 0, 0.2, 1] } }}
      className={`${base} ${variants[variant] ?? variants.feature} ${className}`}
    >
      {children}
    </motion.div>
  );
};

export default FeatureCard;
