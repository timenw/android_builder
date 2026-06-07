# App Icon Requirements for Google Play

## Icon Specifications
- Size: 512 x 512 pixels
- Format: 32-bit PNG with alpha channel
- Color space: sRGB
- Max file size: 1024 KB

## Design Concept
The icon should evoke:
1. **Poetry/Literature** — brush strokes, scroll, or calligraphy elements
2. **Tang Dynasty aesthetic** — elegant, minimal, warm
3. **Moon imagery** — the moon is central to Tang poetry
4. **Warm colors** — terracotta (#C4704B), deep indigo (#3D4F6F), muted gold (#C9A96E)

## Suggested Design
A minimalist icon featuring:
- A crescent moon or full moon
- A single brush stroke suggesting a mountain or a poem line
- Warm gradient background (cream to soft terracotta)
- Clean, modern typography for "300" if space allows

## What to Avoid
- Don't use actual Chinese characters (too small to read at icon size)
- Don't use photos or complex illustrations
- Don't use the same icon as existing poetry apps
- Don't include text that's smaller than 10pt at 512px

## Tools for Creating
- Figma (free, web-based)
- Canva (free, web-based)
- Adobe Illustrator
- Android Studio's Image Asset Studio

## Adaptive Icon (Android 8.0+)
Also create an adaptive icon:
- Foreground layer: 108 x 108 dp (432 x 432 px at 4x)
- Background layer: 108 x 108 dp (432 x 432 px at 4x)
- Safe zone: 66 x 66 dp (center area that won't be masked)

## Current Status
[PLACEHOLDER] — Icon needs to be designed and created.
Once created, place the files at:
- app/src/main/res/mipmap-hdpi/ic_launcher.png (72x72)
- app/src/main/res/mipmap-mdpi/ic_launcher.png (48x48)
- app/src/main/res/mipmap-xhdpi/ic_launcher.png (96x96)
- app/src/main/res/mipmap-xxhdpi/ic_launcher.png (144x144)
- app/src/main/res/mipmap-xxxhdpi/ic_launcher.png (192x192)
- app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml (adaptive icon)
