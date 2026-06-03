# 📝 Changelog

All notable changes to Excel Merger Pro will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [17.7] - 2026-05-31

### ✨ Added
- **All-in-One Merging Mode:** Generates a Master Sheet containing ALL merged data, while keeping individual sheets attached for easy reference
- **Group by Matching Sheet Name:** Automatically merge sheets with the exact same name across multiple workbooks
- **Enhanced Format Support:** Full support for `.xlsx`, `.xls`, `.xlsm` (Macro-enabled), `.csv`, and password-protected files
- **Perfect Bilingual UI:** 100% native translation for both English and Vietnamese interfaces

### 🐛 Fixed
- Fixed freezing issues when merging files with millions of blank/phantom rows
- Improved memory management for large file handling
- Better error handling for corrupted Excel files
- Fixed issue with trailing blank rows not being processed correctly

### 📈 Improved
- Performance optimization for bulk merging operations
- Enhanced user interface responsiveness
- Better column width calculation for diverse data types
- Improved header detection algorithm

### 📚 Documentation
- Updated README with detailed feature explanations
- Added FAQ section addressing common concerns
- Added Pro Tips for optimal results
- Improved quick start guide

---

## [17.5] - 2026-05-15

### ✨ Added
- **Source File Column:** Option to append a "Source File" column to trace data origin
- **Duplicate Header Removal:** Automatically remove duplicate column headers when merging
- **Auto-fit Columns:** Automatically adjust column widths to fit content
- **Header Colorization:** Option to colorize headers for better visibility

### 🐛 Fixed
- Fixed issue where blank rows weren't being skipped properly
- Resolved problem with special characters in file names
- Fixed encoding issues with certain CSV files

### 📈 Improved
- Better handling of merged cells in source files
- Improved CSV parsing for different delimiters
- Enhanced user interface layout
- Better error messages for troubleshooting

---

## [17.0] - 2026-05-01

### ✨ Added
- **Three Merge Modes:**
  - Merge into 1 Master Sheet
  - Keep as Separate Sheets
  - Master + Separate Sheets (All-in-One)
- **Folder Scan Feature:** Select an entire folder to merge all Excel files within it
- **File Selection:** Select individual files for merging
- **Advanced Options:** 
  - Remove duplicate headers
  - Skip blank rows
  - Auto-fit columns
  - Colorize headers
- **Bilingual Interface:** English and Vietnamese support
- **Password-Protected Files:** Support for encrypted Excel files

### 🐛 Fixed
- Initial release with stable core functionality

### 📈 Improved
- Optimized for quick startup and response time
- Clean and intuitive user interface
- Fast processing even with large datasets

---

## [16.0] - 2026-04-15

### ✨ Added
- Basic Excel file merging functionality
- Support for `.xlsx` and `.xls` formats
- Simple single-mode merge (Master Sheet only)
- Basic error handling

### 🐛 Fixed
- Initial testing phase

---

## 🔄 Version History Summary

| Version | Date | Status | Highlights |
|---------|------|--------|-----------|
| **17.7** | May 31, 2026 | ✅ Current | All-in-One mode, Group by Sheet, Optimized for large files |
| **17.5** | May 15, 2026 | ✅ Stable | Source column, Header removal, Auto-fit |
| **17.0** | May 1, 2026 | ✅ Stable | 3 merge modes, Advanced options, Bilingual |
| **16.0** | Apr 15, 2026 | 🔴 Old | Basic merging functionality |

---

## 🚀 Planned Features (Upcoming)

- 🔄 Command-line interface support
- 🖥️ Portable version for USB drives
- 🌍 More language translations (Chinese, French, Spanish)
- 📊 Advanced data validation and cleaning
- 🔒 Enhanced security features
- 🎨 More customization options
- 📱 Integration with cloud storage (Google Drive, OneDrive, Dropbox)
- ⚡ Batch scheduling for automated merging

---

## 📖 How to Update

1. Download the latest version from [Releases](https://github.com/dynamic504/Excel-Merger-Pro/releases)
2. Back up your current version
3. Replace the old file with the new one
4. Double-click to run the updated version

**No installation required!** All versions are standalone.

---

## 🐛 Bug Reports

Found a bug in a previous version? Please [report it](https://github.com/dynamic504/Excel-Merger-Pro/issues/new?template=bug_report.md) so we can fix it!

---

## 💡 Feature Requests

Have an idea for a new feature? We'd love to hear it! [Suggest a feature](https://github.com/dynamic504/Excel-Merger-Pro/issues/new?template=feature_request.md)

---

## 📜 License

Excel Merger Pro is licensed under the GNU General Public License v3.0.

---

**Last Updated:** June 3, 2026  
**Maintainer:** dynamic504
