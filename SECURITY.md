# 🔐 Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in Excel Merger Pro, please **do not** open a public GitHub issue. Instead, please email the security report to:

📧 **vu.thaianh15101985@gmail.com**

Subject: `[SECURITY] Excel Merger Pro Vulnerability Report`

Please include:
- Description of the vulnerability
- Steps to reproduce (if applicable)
- Impact assessment
- Suggested fix (if you have one)

---

## Security Principles

Excel Merger Pro is designed with security as a core principle:

### 🔒 **Data Privacy**
- ✅ **100% Offline:** All processing happens on your computer
- ✅ **No Cloud Upload:** Your data never leaves your machine
- ✅ **No Tracking:** No telemetry, no analytics, no user tracking
- ✅ **No Internet Required:** Fully functional without internet connection
- ✅ **Open Source:** Code is transparent and auditable

### 🛡️ **Antivirus Warnings**
Some antivirus software (Windows Defender, Kaspersky, etc.) may flag the app because:
- It uses **ActiveX** to communicate with Microsoft Excel
- ActiveX requires elevated permissions
- This is **normal for HTA (HTML Application) files**
- **This is NOT a security threat**

### ✅ **Safe to Use**
- No malware, no spyware, no adware
- No unauthorized data collection
- No modifications to system files
- No persistent modifications after closing
- Fully reversible - just delete the file

---

## File Format Security

### **Supported Formats**
- ✅ `.xlsx` - Microsoft Excel 2007+
- ✅ `.xls` - Microsoft Excel 97-2003
- ✅ `.xlsm` - Macro-enabled Excel files
- ✅ `.csv` - Comma-separated values
- ✅ Password-protected files

### **Macro Security**
- Excel macros in `.xlsm` files are **NOT executed**
- Macros are preserved in the output file but require manual enabling
- No hidden code execution
- Safe handling of macro-enabled files

---

## System Requirements & Permissions

### **Permissions Needed**
- Read access to source files
- Write access to destination folder
- Access to Microsoft Excel COM interface
- **No admin rights required** (for normal operation)

### **What Excel Merger Pro Does NOT Do**
- ❌ Does NOT modify system registry
- ❌ Does NOT install background services
- ❌ Does NOT modify Windows settings
- ❌ Does NOT create startup entries
- ❌ Does NOT modify other applications
- ❌ Does NOT store data on cloud servers

### **What Excel Merger Pro DOES Do**
- ✅ Reads Excel files from specified location
- ✅ Creates a new merged Excel file
- ✅ Uses temporary memory for processing
- ✅ Cleans up temporary files after completion

---

## Password-Protected Files

### **Handling Encrypted Files**
If you're merging password-protected Excel files:
1. You'll be prompted to enter the password
2. Password is used only to open the file
3. **Password is NOT stored or transmitted**
4. **Password is NOT included in output file** (unless you enable it)

### **Best Practices**
- ✅ Use strong passwords for sensitive files
- ✅ Only share merged files with authorized users
- ✅ Password-protect output file if it contains sensitive data
- ✅ Delete temporary files after merging

---

## Data Handling

### **Input Files**
- Original files remain **untouched**
- Files are read in read-only mode
- No modifications to source files
- Originals are 100% safe

### **Output Files**
- New merged file is created in your specified location
- You control where the file is saved
- You can password-protect the output if needed
- You decide what to do with the file

### **Temporary Files**
- Temporary data is stored in memory
- Cleaned up automatically after completion
- Not written to disk (by default)
- Deleted even if program crashes

---

## Updates & Patches

### **Security Updates**
- We release security patches promptly
- Always download from official GitHub releases
- Verify file integrity if possible
- Check changelog for security fixes

### **Version Verification**
To verify you're using the official version:
1. Download from: https://github.com/dynamic504/Excel-Merger-Pro/releases
2. Check file size matches the release info
3. File should be named: `ExcelMergerPro_Release.hta`

---

## Third-Party Dependencies

Excel Merger Pro has **minimal dependencies**:
- Microsoft Excel (system requirement, not bundled)
- Windows HTA runtime (built into Windows)
- VBScript (built into Windows)

**No external libraries or packages are bundled.**

---

## Antivirus & SmartScreen

### **Windows Defender Warning**
You may see a "SmartScreen" warning:
- This is because the app is unsigned
- Signing requires an expensive certificate
- The app is still safe to use
- Click "More info" → "Run anyway"

### **Other Antivirus Software**
If your antivirus flags the app:
1. It's likely a false positive
2. The source code is available for review
3. No malicious code is present
4. You can temporarily disable the antivirus

### **Submitting for Whitelisting**
To get the app whitelisted by antivirus vendors:
1. Contact the vendor directly
2. Provide GitHub repository link
3. Request file hash verification
4. Share code for review

---

## Responsible Disclosure

If you discover a vulnerability:

1. **Don't** open a public issue
2. **Don't** share vulnerability details publicly
3. **Do** email us immediately at: vu.thaianh15101985@gmail.com
4. **Do** give us reasonable time to respond (7-14 days)
5. **Do** allow time for a fix before public disclosure

We appreciate your responsible disclosure and will:
- Acknowledge receipt within 24 hours
- Provide status updates
- Fix the issue promptly
- Credit you in the release notes (if desired)

---

## Compliance & Certifications

- ✅ **Open Source:** GPL-3.0 license
- ✅ **Transparent:** Full source code available
- ✅ **No Tracking:** No analytics or telemetry
- ✅ **No Ads:** Ad-free and bloat-free
- ✅ **User Focused:** Privacy-first design

---

## Questions?

For security questions, please email:  
📧 **vu.thaianh15101985@gmail.com**

For bug reports, use [GitHub Issues](https://github.com/dynamic504/Excel-Merger-Pro/issues)

---

**Last Updated:** June 3, 2026  
**Version:** 1.0

---

*Excel Merger Pro is committed to maintaining the highest standards of security and user privacy.*
