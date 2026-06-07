# 300 Tang Poems - Google Play Launch Checklist

## Pre-Launch Requirements

### Google Play Developer Account
- [ ] Register for Google Play Developer account ($25 one-time fee)
- [ ] Complete identity verification
- [ ] Accept Developer Distribution Agreement

### App Build
- [ ] Generate signed release APK or App Bundle (AAB)
- [ ] Test release build on multiple devices
- [ ] Verify all features work correctly
- [ ] Test in-app purchase flow (use Google Play test environment)
- [ ] Verify privacy policy loads correctly in WebView

### Store Listing
- [ ] App name: "300 Tang Poems"
- [ ] Short description (80 chars max)
- [ ] Full description (4000 chars max)
- [ ] App icon (512x512 PNG)
- [ ] Feature graphic (1024x500)
- [ ] Screenshots (minimum 2, recommended 6-8)
- [ ] Select category: Books & Reference
- [ ] Content rating: Complete questionnaire (Everyone)
- [ ] Privacy policy URL
- [ ] Contact email
- [ ] Website URL (optional)

### Pricing & Distribution
- [ ] Set price: Free with in-app purchase
- [ ] Configure in-app product: "poem_premium_lifetime" at $0.99
- [ ] Select distribution countries
- [ ] Accept US export compliance (if distributing to US)

### Content Rating Questionnaire
- [ ] Complete IARC content rating questionnaire
- [ ] Expected rating: Everyone
- [ ] No violence, no sexual content, no gambling

### App Signing
- [ ] Generate upload key (or let Google manage)
- [ ] Keep upload key safe (you'll need it for updates)
- [ ] Create release keystore

## In-App Purchase Setup

### Google Play Console
- [ ] Go to Monetize > Products > In-app products
- [ ] Create product ID: poem_premium_lifetime
- [ ] Set price: $0.99 (or equivalent in local currency)
- [ ] Add title: "Premium — Lifetime Access"
- [ ] Add description: "Unlock unlimited favorites, all themes, poetry cards without watermarks, audio readings, and export."
- [ ] Set to Active
- [ ] Add tax information if required

### Testing
- [ ] Add test accounts in Google Play Console (Settings > License Testing)
- [ ] Test purchase flow with test account
- [ ] Verify purchase acknowledgment works
- [ ] Test "Restore Purchases" functionality

## Post-Launch

### Monitoring
- [ ] Monitor crash reports in Google Play Console
- [ ] Check user reviews regularly
- [ ] Respond to user feedback
- [ ] Track in-app purchase metrics

### Updates
- [ ] Plan first update (bug fixes, user feedback)
- [ ] Keep targetSdk up to date
- [ ] Update privacy policy if data practices change

## Important Notes

### GDPR Compliance
- Privacy policy is accessible within the app
- No personal data is collected
- Users can delete all data by clearing app data
- Data is stored locally only

### COPPA Compliance
- App is suitable for all ages
- No data collection from children
- No ads or third-party trackers

### App Review Guidelines
- App must function as described
- In-app purchases must work correctly
- Privacy policy must be accessible
- App must not crash or have major bugs
- Content must match the stated rating

## Estimated Timeline
1. Developer account setup: 1-2 days (including verification)
2. Store listing preparation: 1 day
3. In-app purchase setup: 1 hour
4. App review: 1-7 days (first submission may take longer)
5. Total: ~1 week

## Cost Summary
- Google Play Developer account: $25 (one-time)
- App hosting: Free
- In-app purchase fee: Google takes 15% of revenue (first $1M/year), then 30%
- No additional costs for updates
