
/**
 * Spatial Transition — 0.45s cubic-bezier (Playwright-verified)
 * Verified: 0.45s cubic-bezier(0.4, 0, 0.2, 1)
 */
export const standardTransition = {
  type: "tween",
  ease: [0.4, 0, 0.2, 1],
  duration: 0.45,
};

/**
 * Rapid Transition — 0.2s (Playwright-verified)
 * Verified: 0.2s
 */
export const rapidTransition = {
  type: "tween",
  ease: "easeOut",
  duration: 0.2,
};

/**
 * Card Hover Variants — translateY(-3px) + shadow (Playwright-verified)
 * Verified: translateY(-3px) + shadow elevation
 */
export const cardHoverVariants = {
  initial: {
    y: 0,
    boxShadow: "0px 4px 12px rgba(0,0,0,0.08)",
  },
  hover: {
    y: -3,
    boxShadow: "0px 10px 30px rgba(0,0,0,0.12)",
    transition: rapidTransition,
  },
};

/**
 * Entrance Variants — 0.45s standard cubic-bezier (Playwright-verified)
 * Verified: 0.45s standard cubic-bezier
 */
export const entranceVariants = {
  hidden: {
    opacity: 0,
    y: 20,
  },
  visible: {
    opacity: 1,
    y: 0,
    transition: standardTransition,
  },
};

/**
 * Shimmer Animation — shimmer_lrn keyframes (Playwright-verified)
 * Verified: shimmer_lrn keyframes
 */
export const shimmerVariants = {
  animate: {
    backgroundPosition: ["-468px 0", "468px 0"],
    transition: {
      repeat: Infinity,
      duration: 1.2,
      ease: "linear",
    },
  },
};
