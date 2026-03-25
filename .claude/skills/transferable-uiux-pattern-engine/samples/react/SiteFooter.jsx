import React from 'react';

/**
 * SiteFooter — Brand-neutral footer component
 *
 * Extracted system patterns (manually verified source site):
 *   bg:        #e9f1fc (light tinted surface — confirmed .ftr-new-inner)
 *   max-width: 1100px inner container (confirmed)
 *   layout:    4-column grid on desktop, 1-column on mobile
 *
 * Adapt: replace [YourBrand], [Your Tagline], and nav link labels.
 */
const SiteFooter = () => {
  const productLinks = ['Feature One', 'Feature Two', 'Feature Three', 'Feature Four', 'Feature Five'];
  const companyLinks = ['About', 'Blog', 'Careers', 'Press'];
  const legalLinks   = ['Privacy Policy', 'Terms & Conditions'];

  return (
    <footer className="bg-[#e9f1fc] py-16">
      <div className="max-w-[1100px] mx-auto px-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">

        {/* Brand column */}
        <div className="lg:col-span-1">
          <div className="mb-4 font-black text-[#193f68] text-2xl tracking-tighter">
            [YourBrand]
          </div>
          <p className="text-[#4b5661] text-sm leading-relaxed mb-6">
            [Your tagline or 1-2 sentence brand description.]
          </p>
          <div className="flex gap-3">
            {['Twitter', 'LinkedIn', 'YouTube', 'Instagram'].map(s => (
              <div
                key={s}
                aria-label={s}
                className="w-8 h-8 rounded-full bg-white/60 border border-[#a6d8fa]/50 flex items-center justify-center text-xs text-[#86949d] cursor-pointer hover:opacity-80 transition-opacity"
              >
                {s[0]}
              </div>
            ))}
          </div>
        </div>

        {/* Product links */}
        <div>
          <h3 className="text-[#193f68] font-bold mb-4 text-sm uppercase tracking-wide">Product</h3>
          <ul className="space-y-3">
            {productLinks.map(link => (
              <li key={link}>
                <a href="#" className="text-sm text-[#4b5661] hover:text-[var(--color-action,#fe6724)] transition-colors">
                  {link}
                </a>
              </li>
            ))}
          </ul>
        </div>

        {/* Company links */}
        <div>
          <h3 className="text-[#193f68] font-bold mb-4 text-sm uppercase tracking-wide">Company</h3>
          <ul className="space-y-3">
            {companyLinks.map(link => (
              <li key={link}>
                <a href="#" className="text-sm text-[#4b5661] hover:text-[var(--color-action,#fe6724)] transition-colors">
                  {link}
                </a>
              </li>
            ))}
          </ul>
        </div>

        {/* App / download column */}
        <div>
          <h3 className="text-[#193f68] font-bold mb-4 text-sm uppercase tracking-wide">Get the App</h3>
          <p className="text-[#4b5661] text-xs leading-relaxed mb-4">
            [App download pitch — one sentence.]
          </p>
          <div className="space-y-2">
            <button className="w-full bg-white border border-[#cacaca] rounded-[5px] py-2 px-4 flex items-center gap-3 text-xs font-bold text-[#111111] hover:shadow-sm transition-shadow">
              <div className="w-4 h-4 bg-black rounded-sm" />
              Google Play
            </button>
            <button className="w-full bg-[#193f68] text-white rounded-[5px] py-2 px-4 flex items-center gap-3 text-xs font-bold hover:opacity-90 transition-opacity">
              <div className="w-4 h-4 bg-white rounded-sm" />
              App Store
            </button>
          </div>
        </div>
      </div>

      {/* Bottom bar */}
      <div className="max-w-[1100px] mx-auto px-4 mt-12 pt-6 border-t border-[#a6d8fa]/50 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-[#86949d]">
        <span>© {new Date().getFullYear()} [YourBrand]. All rights reserved.</span>
        <div className="flex gap-4">
          {legalLinks.map(l => (
            <a key={l} href="#" className="hover:text-[#193f68] transition-colors">{l}</a>
          ))}
        </div>
      </div>
    </footer>
  );
};

export default SiteFooter;
