/**
 * Google Analytics 4 - Unified Configuration
 * 
 * INSTRUCTIONS:
 * 1. Replace 'G-XXXXXXXXXX' with your actual Measurement ID.
 * 2. This file is automatically loaded by all pages on phonenumbergenerator.dev
 */

const MEASUREMENT_ID = 'G-QW70W4LDZ3'; // <--- REPLACE THIS ID

// Dynamically load the GA4 script
const gaScript = document.createElement('script');
gaScript.async = true;
gaScript.src = `https://www.googletagmanager.com/gtag/js?id=${MEASUREMENT_ID}`;
document.head.appendChild(gaScript);

// Initialize dataLayer and gtag
window.dataLayer = window.dataLayer || [];
function gtag() {
    window.dataLayer.push(arguments);
}
gtag('js', new Date());
gtag('config', MEASUREMENT_ID);

console.log('Antigravity GA4 Engine Initialized:', MEASUREMENT_ID);
