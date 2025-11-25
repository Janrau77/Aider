That's a very good point. On a refurbished machine, it's wise to be thorough. The license could be the original OEM license tied to the motherboard, or a new one provided by the refurbisher.

Here's a more comprehensive plan to ensure you save the correct license information. You should do this while booted into Windows 10.

### 1. Check for a Digital License (Most Important)

Modern Windows 10/11 activation often doesn't rely on you knowing the key. It's tied to your hardware and your Microsoft account.

*   Go to **Settings** > **Update & Security** > **Activation**.
*   Look at the activation status. If it says **"Windows is activated with a digital license linked to your Microsoft account"**, you are in the best possible position.
*   **What this means:** When you reinstall Windows 10 Pro on the same laptop in the future, you can skip the product key entry. Once you connect to the internet and sign in with the same Microsoft account, it will automatically reactivate.

### 2. Retrieve the OEM Key from Firmware

This command attempts to read the original product key that was embedded in the laptop's motherboard firmware by the manufacturer (e.g., Lenovo).

*   Open **Command Prompt as Administrator** or **PowerShell as Administrator**.
*   Type the following command and press Enter:
    ```
wmic path softwarelicensingservice get OA3xOriginalProductKey
    ```
*   If a key is stored in the firmware, it will be displayed. **Copy and save this key.** This is often the most reliable key for the machine itself.

### 3. Use a Third-Party Tool

For a simple, all-in-one view, you can use a free, reputable key-finder utility. A great option is **ShowKeyPlus**, which you can get from the Microsoft Store.

When you run it, it will clearly show you:
*   **Installed Key:** The product key your current Windows installation is using.
*   **OEM Key:** The key embedded in the firmware (if present).
*   **Original Key:** The key that was used during the initial installation of the current OS.

By checking for a **digital license** and using the command or a tool to find the **OEM key**, you will have the best possible chance of successfully reactivating your paid copy of Windows 10 Pro if you ever need to reinstall it.