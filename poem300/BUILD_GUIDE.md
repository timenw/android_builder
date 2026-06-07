# 300 Tang Poems - Build Guide

## Prerequisites

### 1. Install JDK 17+
```bash
# Ubuntu/Debian
sudo apt-get install openjdk-17-jdk-headless

# macOS
brew install openjdk@17

# Verify
java -version  # Should show 17.x
```

### 2. Install Android SDK
Option A: Install Android Studio (recommended)
- Download from https://developer.android.com/studio
- Let it install the SDK automatically
- Note the SDK path (usually ~/Android/Sdk)

Option B: Command Line Tools only
```bash
# Download command line tools
wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip
unzip commandlinetools-linux-9477386_latest.zip -d /opt/android-sdk/cmdline-tools/
mv /opt/android-sdk/cmdline-tools/cmdline-tools /opt/android-sdk/cmdline-tools/latest

# Set environment variables
export ANDROID_HOME=/opt/android-sdk
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools

# Install required SDK components
sdkmanager "platforms;android-34" "build-tools;34.0.0" "platform-tools"
```

### 3. Set Environment Variables
Add to your ~/.bashrc or ~/.zshrc:
```bash
export ANDROID_HOME=$HOME/Android/Sdk  # or /opt/android-sdk
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools
```

## Build Steps

### 1. Extract the source code
```bash
tar -xzf poem300-source.tar.gz
cd poem300/
```

### 2. Generate gradlew
Since gradlew is not included, generate it:
```bash
# If you have Gradle installed globally
gradle wrapper --gradle-version 8.4

# Or download the wrapper manually
mkdir -p gradle/wrapper
curl -sL https://raw.githubusercontent.com/gradle/gradle/v8.4.0/gradle/wrapper/gradle-wrapper.jar -o gradle/wrapper/gradle-wrapper.jar
curl -sL https://raw.githubusercontent.com/gradle/gradle/v8.4.0/gradle/wrapper/gradle-wrapper.properties -o gradle/wrapper/gradle-wrapper.properties

# Create gradlew script (Linux/macOS)
cat > gradlew << 'EOF'
#!/bin/sh
##############################################################################
# Gradle start up script for POSIX
##############################################################################
APP_HOME=$( cd "${0%/*}" > /dev/null && pwd -P ) || exit
CLASSPATH=$APP_HOME/gradle/wrapper/gradle-wrapper.jar
exec java -classpath "$CLASSPATH" org.gradle.wrapper.GradleWrapperMain "$@"
EOF
chmod +x gradlew
```

### 3. Build Debug APK
```bash
./gradlew assembleDebug
```
Output: app/build/outputs/apk/debug/app-debug.apk

### 4. Build Release APK (for Google Play)
```bash
# First, generate a keystore (keep this safe!)
keytool -genkey -v -keystore poem300-release.keystore -alias poem300 -keyalg RSA -keysize 2048 -validity 10000

# Build release APK
./gradlew assembleRelease
```
Output: app/build/outputs/apk/release/app-release.apk

### 5. Build App Bundle (recommended for Google Play)
```bash
./gradlew bundleRelease
```
Output: app/build/outputs/bundle/release/app-release.aab

## Signing Configuration

Before building release, add signing to app/build.gradle.kts:
```kotlin
android {
    signingConfigs {
        create("release") {
            storeFile = file("poem300-release.keystore")
            storePassword = "YOUR_STORE_PASSWORD"
            keyAlias = "poem300"
            keyPassword = "YOUR_KEY_PASSWORD"
        }
    }
    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("release")
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        }
    }
}
```

## Troubleshooting

### "SDK not found"
Make sure ANDROID_HOME is set correctly:
```bash
echo $ANDROID_HOME
ls $ANDROID_HOME/platforms/
```

### "Gradle wrapper not found"
Generate it as shown in step 2 above.

### "Could not resolve dependencies"
Make sure you have internet access and the repositories are accessible. The build.gradle.kts uses google() and mavenCentral().

### Build fails with memory error
```bash
export GRADLE_OPTS="-Xmx2048m"
./gradlew assembleDebug
```

## Project Structure
```
poem300/
├── app/
│   ├── src/main/
│   │   ├── assets/poems.db          # 300 poems database
│   │   ├── java/com/poem300/        # Kotlin source code
│   │   │   ├── MainActivity.kt
│   │   │   ├── MainViewModel.kt
│   │   │   ├── billing/BillingManager.kt
│   │   │   ├── data/                # Database + Repository
│   │   │   └── ui/                  # Screens + Theme
│   │   └── res/                     # Resources
│   └── build.gradle.kts
├── build.gradle.kts
├── settings.gradle.kts
└── gradle/wrapper/
```

## Key Dependencies
- Kotlin 1.9.20
- Jetpack Compose BOM 2023.10.01
- Room 2.6.1
- Navigation Compose 2.7.5
- Google Play Billing 6.1.0
- Target SDK: 34
- Min SDK: 26 (Android 8.0)
