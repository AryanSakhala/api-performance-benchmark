# Recording Script: Expense Audit

Read lines in quotes aloud. Lines in [brackets] are actions: do not say them. Adjust UI labels if your LibreOffice or VS Code version differs. Swap the Part 0 opening for the exact template in the Writer Guidelines and keep it under 20 seconds.

## Before recording
- Log in as the tasker user. Show the menu bar clock with seconds, the Dock, and the Accessibility Inspector.
- Put `expenses_raw.csv` in `Desktop/input`. Create an empty `Desktop/deliverables`.
- Keep the task description document open.
- Copy the `input` folder into `deliverables` before Part 3 and say so aloud.

## Rules
- Say what you click, where it is, and why, before you click. Pause the mouse 1 second after each click. Narrate every click, including close buttons.
- Say each typed line aloud, then describe the result. Close each app before opening the next.
- Typing must stay under 35% of the video. No silence over 45 seconds.

## Part 0. Opening (under 20 seconds)
[Task description fills the screen.]
"Hello. In this task, I am a freelance bookkeeper. My goal is to clean a messy yearly expense CSV file, find duplicate and miscategorized transactions, and produce a category summary workbook with a chart and a short written audit report. The apps I will use are Finder, LibreOffice Calc, Visual Studio Code, and Terminal. I will now minimize this task description by clicking the yellow button at the top left of this window."

## Part 1. Finder: find the input file
"First, I will click the Finder icon, the blue and white smiling face at the far left of the Dock."
"A Finder window opened. In the sidebar on the left, I will click Desktop, because my working folders are there."
"I can see two folders: input and deliverables. I will double-click the input folder to open it."
"Inside is one file, expenses underscore raw dot c s v, with about one hundred and forty-six made-up transactions in four columns: date, vendor, amount, and category. I made this data myself, so it has no personal information."
"I will click the red button at the top left of the Finder window to close it."

## Part 2. LibreOffice Calc: inspect the raw data
"I will click the LibreOffice icon in the Dock."
"I will click Open File on the left of the Start Center. In the dialog, I will click Desktop in the sidebar, double-click the input folder, then double-click expenses underscore raw dot c s v."
"A Text Import window opened. The separator is comma, which is correct. I will click OK at the bottom right."
"Column A is the date, B the vendor, C the amount, D the category. I will scroll down with the mouse wheel to look for problems."
"In column D, Travel appears with different capitalization and an extra trailing space, so a spreadsheet would count each spelling as a separate category."
"In column A, some date cells are empty, so those transactions cannot be placed in a month."
"Here, two rows have the same date, vendor, amount, and category. These are duplicates and would be counted twice."
"I found three problems: inconsistent categories, missing dates, and duplicates. I will fix them in a Python notebook. I will close this file by clicking the red button at the top left. If a save prompt appears, I will click Don't Save, because I changed nothing."

## Part 3. Visual Studio Code: write the notebook
"I will click the blue VS Code icon in the Dock."
"I will click File in the menu bar at the top of the screen, then Open Folder. I will click Desktop, click the deliverables folder once, and click Open at the bottom right. If a trust prompt appears, I will click Yes, I trust the authors, because the folder is mine."
"In the Explorer panel on the left, the folder is empty. I will click the New File icon at the top of the Explorer panel and type expense underscore audit dot i p y n b, then press Enter."
"The notebook opened on the right. I will click the plus Markdown button in the toolbar to add a text cell."

For each cell pair: say the explanation, add a Markdown cell and type it, click plus Code, say each code line aloud, type it, press Shift+Enter, then read the result.

### Cell 1 (markdown: title)
```
# Expense Audit
Clean the raw expense CSV, flag problems, and summarize spend by category.
```
"I will press Shift and Enter to finish the text cell."

### Cell pair 2: imports
Markdown: "## Step 1: Imports. We import csv to read and write the spreadsheet files, and Counter to add up spend per category. Running this cell prints nothing."
```python
import csv
from collections import Counter
```
"I pressed Shift and Enter. If asked for a kernel I select Python 3. Nothing printed, which is expected for imports."

### Cell pair 3: settings
Markdown: "## Step 2: Settings. This cell stores the input path, the two output file names, and the column names, so I only change them in one place."
```python
INPUT = "input/expenses_raw.csv"
CLEAN = "expenses_clean.csv"
FLAGGED = "expenses_flagged.csv"
FIELDS = ["date", "vendor", "amount", "category"]
```
"Nothing printed, because this cell only stores values."

### Cell pair 4: load the data
Markdown: "## Step 3: Load the raw data. This cell opens the input CSV, reads every row into a list, prints the row count, and shows the first five rows."
```python
with open(INPUT, newline="") as f:
    rows = list(csv.DictReader(f))
print(f"Rows read: {len(rows)}")
rows[:5]
```
"The output says Rows read: 146, and shows the first five rows, so the file loaded correctly."

### Cell pair 5: normalize
Markdown: "## Step 4: Normalize text. This cell trims extra spaces and converts category names to Title Case, so travel with a space and TRAVEL both become Travel. Then it shows the distinct categories."
```python
for row in rows:
    row["vendor"] = row["vendor"].strip()
    row["category"] = row["category"].strip().title()
    row["date"] = row["date"].strip()
sorted({r["category"] for r in rows})
```
"The output lists exactly six categories: Marketing, Meals, Office Supplies, Software, Travel, and Utilities. The spelling variants are merged."

### Cell pair 6: duplicates and missing dates
Markdown: "## Step 5: Remove duplicates and flag missing dates. If the same date, vendor, amount, and category was already seen, it counts a duplicate and skips it. Rows with no date go to a flagged list, and the rest go to the clean list. It prints three counts."
```python
seen = set()
clean, flagged, duplicates = [], [], 0
for row in rows:
    key = (row["date"], row["vendor"], row["amount"], row["category"])
    if key in seen:
        duplicates += 1
        continue
    seen.add(key)
    (clean if row["date"] else flagged).append(row)
print(f"Duplicates removed: {duplicates}")
print(f"Rows flagged (missing date): {len(flagged)}")
print(f"Rows kept: {len(clean)}")
```
"The output says Duplicates removed: 7, Rows flagged: 5, Rows kept: 134. Seven plus five plus one hundred and thirty-four is one hundred and forty-six, so every row is accounted for."

### Cell pair 7: save results
Markdown: "## Step 6: Save the results. This cell writes the clean rows to expenses underscore clean dot csv and the flagged rows to expenses underscore flagged dot csv, each with a header line."
```python
for path, data in ((CLEAN, clean), (FLAGGED, flagged)):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(data)
print("Wrote", CLEAN, "and", FLAGGED)
```
"The output names the two files, and they appeared under deliverables in the Explorer panel."

### Cell pair 8: totals
Markdown: "## Step 7: Total spend per category. This cell adds up the amount for each category in the clean data and prints totals from highest to lowest."
```python
totals = Counter()
for row in clean:
    totals[row["category"]] += float(row["amount"])
for category, total in totals.most_common():
    print(f"{category}: {total:.2f}")
```
"Office Supplies is highest at 17,273.09, then Travel 14,090.25, Utilities 9,760.64, Meals 9,132.84, Marketing 9,018.58, and Software 6,743.02."

"I will press Command and S to save, then click the red button at the top left to close VS Code."

## Part 4. Terminal: confirm the output files
"I will click the black Terminal icon in the Dock."
"I will type cd space Desktop slash deliverables and press Enter. The prompt now ends with deliverables."
"I will type l s and press Enter. The Terminal printed expense underscore audit dot i p y n b, expenses underscore clean dot csv, expenses underscore flagged dot csv, and input."
"I will type w c space dash l space expenses underscore clean dot csv and press Enter. It printed 135, which is 134 data rows plus the header, matching the notebook."
"I will click the red button at the top left to close Terminal. If a prompt appears, I will click Terminate."

## Part 5. LibreOffice Calc: summary workbook
"I will open LibreOffice from the Dock, click Open File, click Desktop, double-click deliverables, double-click expenses underscore clean dot csv, then click OK in Text Import."
"I will click cell A1, then press Command and A to select all the data."
"I will click the Insert menu, then Pivot Table, then Insert or Edit Pivot Table. I will leave Current selection chosen and click OK."
"In the layout window, I will drag category into Row Fields and amount into Data Fields. It shows Sum, amount, which is the total I want. I will click OK."
"A new sheet has the pivot table, with each category and its total spend, and a Total Result row."
"I will drag across the category rows and totals, not including Total Result, to select them. I will click Insert, then Chart, click Bar in the list on the left, and click Finish. Office Supplies has the tallest bar. I will click an empty cell to leave chart editing."
Check formula: "I will click an empty cell to the right of the pivot table, type equals SUM, select the amount column on the clean data sheet, close the parenthesis, and press Enter. The result equals the pivot Total Result, so no rows were lost."
"I will click File, then Save As, type expense underscore summary, choose ODF Spreadsheet, click Desktop, double-click deliverables, and click Save. If a prompt appears, I will click Use ODF Format. I will close Calc with the red button."

## Part 6. VS Code: audit notes
"I will click the VS Code icon in the Dock. The deliverables folder is open. I will click the New File icon in the Explorer panel, type audit underscore notes dot m d, and press Enter." Type, saying each line aloud:
```
# Audit Notes
Top categories: Office Supplies 17,273.09, Travel 14,090.25, Utilities 9,760.64.
Issues fixed: 7 duplicate rows removed, 5 rows flagged for a missing date, and 10 category spelling variants merged.
Recommendation: review Office Supplies spending, the largest category, for possible savings.
```
"I will press Command and S to save, then close VS Code with the red button."
(If you used AI to prepare any text before recording, say so in the metadata, not in the video. Do not use AI during recording.)

## Part 7. Finder: show the deliverables
"I will click the Finder icon, click Desktop in the sidebar, and double-click the deliverables folder."
"Inside are: the input folder with expenses underscore raw dot c s v, my starting file; expense underscore audit dot i p y n b, the notebook with my code; expenses underscore clean dot csv, with 134 rows; expenses underscore flagged dot csv, with the 5 missing-date transactions; expense underscore summary dot o d s, with the pivot table and chart; and audit underscore notes dot m d, my written report." Move the mouse over each file as you name it.

## Part 8. Epilogue (about 3.5 minutes, 4 maximum)
Stay on the open deliverables folder. Do not say you are stopping the recording.

"This is the epilogue, where I summarize the task. My goal was to take a messy yearly expense CSV, clean it, and produce a category summary with a chart and a short audit report. I started with one input file of about one hundred and forty-six made-up transactions. I finished with a clean data file, a flagged file, a summary workbook with a pivot table and a bar chart, and a written audit note, all in the deliverables folder on the Desktop.

First, verification. In the notebook, the counts add up: seven duplicates, five missing dates, and one hundred and thirty-four clean rows make one hundred and forty-six. In Terminal, the clean file had one hundred and thirty-five lines, which is the rows plus the header. In LibreOffice Calc, a separate sum of the clean amounts matched the pivot table total, so no money was lost or counted twice. The category check showed exactly six clean names.

Second, my approach. I looked at the raw data in Calc first, because a bookkeeper should see the problems before writing code. I used a Python notebook because each step can be run and checked on its own. I normalized text before removing duplicates, because rows that differ only by capitalization or a trailing space would otherwise slip through. I flagged missing dates instead of deleting them, because a missing date is a question for the client, not a reason to discard a real expense.

Third, challenges. The hardest judgment was what counts as a duplicate. Two legitimate purchases can be identical, like two coffees at the same cafe on one day. I matched on date, vendor, amount, and category, which is strict enough to avoid removing real purchases, though a human should still review the removed rows. I also kept the totals trustworthy by checking them two different ways.

Fourth, quality. The output files have clear headers and consistent category names, so anyone can open them in any spreadsheet program. The notebook has a text explanation above each code cell, so a reviewer can follow the logic. With more time, I would match similar vendor names and add a monthly breakdown so seasonal spending is visible.

Finally, a reflection. This workflow mirrors real small-business bookkeeping before tax filing: inspect, clean, summarize, verify, and recommend. Office Supplies is the first place I would look for savings. The key lesson is that cleaning data is about decisions: what to keep, what to remove, and what to ask about, while showing that the numbers still add up. Thank you."
