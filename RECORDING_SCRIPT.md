# Recording Script: Expense Audit (full, click-by-click, about 25 to 30 minutes)

How to use this: lines in quotes are spoken aloud, word for word. Lines in [brackets] are physical actions: do them, do not say them. Every action is announced BEFORE you do it (what, where, why), then done, then the result is described AFTER. After every click, hold the mouse perfectly still for 1 second.

Replace the opening in Part 0 with the exact template in the Writer Guidelines (reviewer: opening must be under 20 seconds including closing the description text).

## Checklist before you press record (do not narrate)
- Log in to the dedicated tasker macOS user, never your own. Rename the Mac to a neutral name so no personal name shows in Terminal or Finder paths.
- Menu bar clock shows seconds. Dock visible. Accessibility Inspector pinned to the Dock and running, visible the whole time.
- `Desktop/input/expenses_raw.csv` exists. `Desktop/deliverables` exists and is empty except a copy of `input`. Nothing else on the Desktop.
- No app open except the task description document. No AI tools, no restricted apps, no TextEdit.
- Plan: Finder, LibreOffice Calc, VS Code, Terminal. Close each app before opening the next so windows never overlap and nothing is full screen.
- Typing must stay at 35% of the video or less. No silence over 45 seconds. Speak at a normal pace.

## Universal narration pattern (use on EVERY action)
1. WHAT: "I will click ..." / "I will double-click ..." / "I will press ... on the keyboard."
2. WHERE: "... at the top left of the screen / the third icon from the left in the Dock / the left sidebar ..."
3. WHY: "... because ..."
4. [Move the mouse slowly to the target. Click. Hold still 1 second.]
5. RESULT: "I clicked it. Now ... is showing / the window opened / the Terminal printed ..."

---

## PART 0. Opening (target 15 to 18 seconds) [about 0:00]
[The task description document fills the screen. The mouse rests in the middle of the document. Do not scroll.]
"Hello. In this task I play the role of a freelance bookkeeper. My goal is to clean a messy yearly expense CSV file, find duplicate and miscategorized transactions, and produce a category summary workbook with a chart and a short written audit report. I will use Finder, LibreOffice Calc, Visual Studio Code, and Terminal. Now I will minimize this task description."
"To do that, I will move my mouse to the top left corner of this document window, where there are three small colored circles. I will click the yellow one, the minimize button, because I want the screen clear before I start."
[Move mouse slowly to the yellow circle. Click. Hold 1 second.]
"I clicked the yellow button, and the task description is now minimized into the Dock."

## PART 1. Finder: look up the starting material [about 0:20 to 2:30]
"My first step is to look at my starting file. I will open Finder."
"I will move my mouse down to the Dock at the bottom of the screen. Finder is the first icon on the far left of the Dock, a blue and white smiling face. I will click it, because Finder is where I browse my files."
[Click. Hold 1 second.]
"A Finder window opened in the middle of the screen. It is not full screen, so I can still see the Dock at the bottom and the menu bar with the clock at the top."
"On the left side of this window is the sidebar, a gray list of places. I will move my mouse to the item called Desktop, about the middle of that list, and click it, because my working folders are on the Desktop."
[Move. Click Desktop. Hold 1 second.]
"I clicked Desktop. The main area on the right of the window now shows the contents of my Desktop. I can see two folders: one called input and one called deliverables."
"The input folder holds my starting material. The deliverables folder is where I will save all my finished work. At this moment, deliverables only contains a copy of the input folder."
"I will double-click the folder called input, because I want to see which file is inside. Double-click means two quick clicks in a row on the folder name."
[Move to input. Double-click. Hold 1 second.]
"I double-clicked input. It opened, and inside there is exactly one file, called expenses underscore raw dot c s v."
"This is a file I wrote myself. It holds about one hundred and forty-six made-up business transactions for one year. It has four columns: date, vendor, amount, and category. Because all the data is invented by me, it contains no real names, no real accounts, and no copyrighted material."
"I will single-click the file once to select it, so you can see it highlighted. I am doing this to confirm the exact file name."
[Click the file once. Hold 1 second.]
"The file name is highlighted. It reads expenses underscore raw dot c s v."
"Now I will right-click the file, which means pressing the secondary button on the mouse or trackpad with two fingers, because I want to check its size and kind with Get Info."
[Right-click. A menu appears.]
"A context menu appeared next to the file. I will move down to the option called Get Info, about a third of the way down the menu, and click it."
[Click Get Info. Hold 1 second.]
"A small Info window opened. It says the kind is Comma Separated Values Text File, and the size is a few kilobytes. That means it is a small plain text file, safe to open in any spreadsheet program. I will close this Info window by clicking the red circle at the top left of the Info window."
[Click red. Hold 1 second.]
"The Info window is closed. I am satisfied that this is the right starting file."
"Now I will close Finder, because I want only one app open at a time. I will click the red circle at the top left corner of the Finder window."
[Click red. Hold 1 second.]
"Finder is closed, and I can see my Desktop again."

## PART 2. LibreOffice Calc: inspect the raw data [about 2:30 to 7:00]
"My second step is to look at the raw data in a spreadsheet, so I can find the problems before I write any code. I will open LibreOffice."
"I will move my mouse to the Dock and find the LibreOffice icon. It is the white and green document icon near the middle of the Dock. I will click it, because LibreOffice Calc is my spreadsheet program."
[Click. Wait. Hold 1 second.]
"LibreOffice is opening. The Start Center appeared. It shows a column of buttons on the left side and recent documents on the right."
"I will click the button called Open File, which is the second button from the top in the left column, because I want to open my CSV."
[Click. Hold 1 second.]
"A file dialog opened. It looks like a Finder window. In the sidebar on the left, I will click Desktop, because the input folder is there."
[Click Desktop. Hold 1 second.]
"I clicked Desktop. Now I will double-click the folder called input, in the main list on the right."
[Double-click. Hold 1 second.]
"The folder opened and shows one file. I will double-click expenses underscore raw dot c s v to open it."
[Double-click. Hold 1 second.]
"A window called Text Import appeared. This is LibreOffice asking how to split the CSV into columns."
"At the top, I can see the character set, which is Unicode, and the language, which is English. In the Separator Options section in the middle, the Comma box is checked. That is correct, because a CSV file separates columns with commas. At the bottom is a preview showing four columns."
"I will leave the defaults unchanged and click the OK button at the bottom right of this window."
[Move to OK. Click. Hold 1 second.]
"I clicked OK, and the file opened in LibreOffice Calc. It is a normal spreadsheet with rows and columns."
"Column A holds the date. Column B holds the vendor name. Column C holds the amount in dollars. Column D holds the category. Row one is the header row."
"I will now scroll down slowly with the mouse wheel, by moving two fingers down on the trackpad, so I can look for problems. I am scrolling because there are about one hundred and forty-six rows and I cannot see them all at once."
[Scroll slowly, 2 to 3 seconds per screen. Stop when you see each problem.]
"Problem one, the category names. In column D, here, I see Travel with a capital T. A few rows below it, the same word appears in all lowercase. Here is another one in all capital letters. And here, I will click on this cell, D thirty-one, and look at the formula bar at the top: the word has an extra space at the end. To a computer, each of these spellings is a different category. If I summed spending by category now, Travel would be split into several wrong totals."
"Problem two, the dates. In column A, here, this cell is empty. And another one over here is empty too. These transactions have no date, so I cannot place them in a month or a quarter. I will count five of these in total as I scroll."
"Problem three, duplicates. Here, row twenty-two and row seventy-one have the same date, the same vendor, the same amount, and the same category. They look like the same payment entered twice. If I leave them in, the totals will be too high."
"So the data has three issues: inconsistent category names, missing dates, and duplicate rows. A bookkeeper must fix all three before preparing a report for tax filing. I will fix them with a Python notebook, because a notebook lets me run and check each cleaning step separately."
"I did not change this file, so I will close it without saving. I will move my mouse to the top left corner of this Calc window and click the red circle."
[Click red. Hold 1 second.]
"A prompt asked whether to save changes. I will click Don't Save, the left button in the prompt, because I made no edits."
[Click Don't Save. Hold 1 second.]
"The document closed, and the Start Center is still open. I will close it too, by clicking its red circle at the top left."
[Click red. Hold 1 second.]
"LibreOffice is closed. My Desktop is clear again."

## PART 3. Visual Studio Code: write the notebook (main app) [about 7:00 to 15:30]
"My third step is to write the cleaning code. I will open Visual Studio Code, which I will call VS Code."
"I will move my mouse to the Dock and click the VS Code icon, a blue icon shaped like a folded ribbon, near the middle of the Dock. I am opening it because it can run notebooks, one cell at a time."
[Click. Wait. Hold 1 second.]
"VS Code opened in a window, not full screen. At the top is the menu bar, on the left is a thin bar of icons, and in the middle is a Welcome page."
"I want to work inside my deliverables folder. I will click File in the menu bar at the very top of the screen, the second word from the left after the VS Code name, because the Open Folder command is under it."
[Click File. Hold 1 second.]
"The File menu opened. I will move down to Open Folder and click it."
[Click Open Folder. Hold 1 second.]
"A file dialog opened. In the sidebar on the left, I will click Desktop."
[Click. Hold 1 second.]
"I will click once on the folder called deliverables, to select it. I am not double-clicking, so I do not open it yet."
[Click. Hold 1 second.]
"Now I will click the Open button at the bottom right of the dialog."
[Click. Hold 1 second.]
"A prompt may ask whether I trust the authors of this folder. I will click the button Yes, I trust the authors, because this is my own folder. [If it does not appear, say: No prompt appeared, so I continue.]"
[Click if shown. Hold 1 second.]
"The deliverables folder is open. On the left side is the Explorer panel. It shows the folder name, deliverables, and below it a folder called input, which is my starting material copied here."
"I will click the small arrow next to the folder input, to expand it, because I want to confirm the CSV is inside."
[Click arrow. Hold 1 second.]
"Inside input, there is expenses underscore raw dot c s v. Good. I will click the arrow again to collapse it."
[Click arrow. Hold 1 second.]
"Now I will create the notebook. In the Explorer panel, at the top right of the panel next to the folder name, there are four small icons. The first one, a page with a plus sign, is New File. I will hover the mouse over it first, and a label confirms New File. Then I will click it."
[Hover 1 second. Click. Hold 1 second.]
"A text box appeared in the Explorer panel, asking for the file name. I will type: expense, underscore, audit, dot, i, p, y, n, b. Then I will press the Enter key on the keyboard."
[Type expense_audit.ipynb. Press Enter. Hold 1 second.]
"The file expense underscore audit dot i p y n b was created, and a notebook opened in the large area on the right. The toolbar at the top of the notebook has buttons called plus Code and plus Markdown."

### Typing rhythm for every cell (use it for all 15 cells)
(a) Announce the cell: "I will now add a markdown cell, to explain the next step in plain English."
(b) Click "plus Markdown" at the top of the notebook. Hold 1 second. The cursor is blinking inside the new cell.
(c) Read the text aloud once, then type it slowly while saying nothing extra (typing counts toward the 35% limit, so keep text short).
(d) Press Shift and Enter together to render the text. Say: "I pressed Shift and Enter, so the text turned into a formatted explanation."
(e) Announce: "Now I will click plus Code, to add a code cell below."
(f) Click plus Code. Say each line before typing it. Type it.
(g) Press Shift and Enter. Say: "I pressed Shift and Enter to run the cell." Describe the output in plain words.

### Cell 1: title (markdown)
"I will click the plus Markdown button at the top of the notebook, because I want a title cell first."
[Click. Hold 1 second.]
"I will type a pound sign, a space, and the words Expense Audit. Then I will press Enter, and type one sentence: Clean the raw expense CSV, flag problems, and summarize spend by category."
```
# Expense Audit
Clean the raw expense CSV, flag problems, and summarize spend by category.
```
"I will press Shift and Enter. The text became a large title with a smaller sentence under it."

### Cells 2 and 3: imports
Markdown: "I will click plus Markdown and type: pound pound, space, Step 1, colon, Imports. Press Enter. We import csv to read and write the spreadsheet files, and Counter to add up spend per category. Running this cell prints nothing."
```
## Step 1: Imports
We import csv to read and write the spreadsheet files, and Counter to add up spend per category. Running this cell prints nothing.
```
"Shift and Enter. It rendered as a heading and a sentence."
"Now I will click plus Code. I will type the first line: import, space, csv. I will press Enter, and type the second line: from, space, collections, space, import, space, Counter, with a capital C."
```python
import csv
from collections import Counter
```
"I will press Shift and Enter to run it. At the top of the screen, VS Code asks me to select a kernel. A kernel is the Python engine that runs the cell. I will click the Python 3 option in the list, because it is the Python installed on this Mac."
[Click Python 3. Hold 1 second.]
"The cell ran. A green check mark and a small number appeared on its left. Nothing was printed, which is expected, because imports print nothing."

### Cells 4 and 5: settings
Markdown: "I will click plus Markdown and type: Step 2, Settings. This cell stores the input path, the two output file names, and the column names, so I only change them in one place."
```
## Step 2: Settings
This cell stores the input path, the two output file names, and the column names, so I only change them in one place.
```
"Shift and Enter."
"Now I will click plus Code. I will type, line by line. First: INPUT in capital letters, equals, quote, input, slash, expenses, underscore, raw, dot, csv, quote."
"Second: CLEAN, equals, quote, expenses underscore clean dot csv, quote."
"Third: FLAGGED, equals, quote, expenses underscore flagged dot csv, quote."
"Fourth: FIELDS, equals, an open square bracket, then four quoted words separated by commas: date, vendor, amount, category, and a closing square bracket."
```python
INPUT = "input/expenses_raw.csv"
CLEAN = "expenses_clean.csv"
FLAGGED = "expenses_flagged.csv"
FIELDS = ["date", "vendor", "amount", "category"]
```
"I will press Shift and Enter. Nothing printed, because this cell only stores values for later cells."

### Cells 6 and 7: load the data
Markdown: "Step 3, Load the raw data. This cell opens the input CSV, reads every row into a list, prints the row count, and shows the first five rows."
```
## Step 3: Load the raw data
This cell opens the input CSV, reads every row into a list, prints the row count, and shows the first five rows.
```
"Shift and Enter."
Code, say each line: "with, space, open, open parenthesis, INPUT, comma, newline, equals, two quotes, close parenthesis, as, f, colon. Enter. Notice VS Code indented the next line automatically, by four spaces. rows, equals, list, open parenthesis, csv, dot, DictReader, open parenthesis, f, close parenthesis, close parenthesis. Enter, then press Shift and Tab to move back left. print, open parenthesis, f, quote, Rows read, colon, space, open curly brace, len, open parenthesis, rows, close parenthesis, close curly brace, quote, close parenthesis. Enter. Last line: rows, open square bracket, colon, 5, close square bracket."
```python
with open(INPUT, newline="") as f:
    rows = list(csv.DictReader(f))
print(f"Rows read: {len(rows)}")
rows[:5]
```
"I will press Shift and Enter. The output says Rows read, colon, 146. Under it are the first five rows, each shown as a dictionary with date, vendor, amount, and category. This tells me the file loaded correctly and that I have one hundred and forty-six rows to clean."

### Cells 8 and 9: normalize
Markdown: "Step 4, Normalize text. This cell trims extra spaces and converts category names to Title Case, so travel with a space and TRAVEL both become Travel. Then it shows the distinct categories."
```
## Step 4: Normalize text
This cell trims extra spaces and converts category names to Title Case, so "travel " and "TRAVEL" both become "Travel". Then it shows the distinct categories.
```
Code, say each line: "for, row, in, rows, colon. Enter. Indented: row, open square bracket, quote, vendor, quote, close square bracket, equals, row, open square bracket, quote vendor quote, close square bracket, dot, strip, open and close parentheses. Enter. Same for category, but add dot title after strip. Enter. Same for date. Then press Shift and Tab. Last line: sorted, open parenthesis, open curly brace, r, open square bracket, quote category quote, close square bracket, for, r, in, rows, close curly brace, close parenthesis."
```python
for row in rows:
    row["vendor"] = row["vendor"].strip()
    row["category"] = row["category"].strip().title()
    row["date"] = row["date"].strip()
sorted({r["category"] for r in rows})
```
"I will press Shift and Enter. The output is a list of exactly six categories: Marketing, Meals, Office Supplies, Software, Travel, and Utilities. All the spelling variants I saw in Calc are now merged. For example, travel with a trailing space and TRAVEL are both just Travel."

### Cells 10 and 11: duplicates and missing dates
Markdown: "Step 5, Remove duplicates and flag missing dates. If the same date, vendor, amount, and category was already seen, it counts a duplicate and skips it. Rows with no date go to a flagged list, and the rest go to the clean list. It prints three counts."
```
## Step 5: Remove duplicates and flag missing dates
If the same date, vendor, amount, and category was already seen, it counts a duplicate and skips it. Rows with no date go to a flagged list, and the rest go to the clean list. It prints three counts.
```
Code, say each line: "seen equals set, open and close parentheses. Enter. clean, comma, flagged, comma, duplicates, equals, two empty square brackets separated by a comma, then a comma and zero. Enter. for row in rows, colon. Enter. Indented: key, equals, an open parenthesis, row of date, row of vendor, row of amount, row of category, close parenthesis. Enter. if key in seen, colon. Enter. Indent further: duplicates plus equals 1. Enter. continue. Enter, then Shift and Tab. seen dot add, open parenthesis, key, close parenthesis. Enter. Open parenthesis, clean, if, row of date, else, flagged, close parenthesis, dot append, open parenthesis, row, close parenthesis. Then Shift and Tab twice, and three print lines."
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
"I will press Shift and Enter. The output says: Duplicates removed, 7. Rows flagged, missing date, 5. Rows kept, 134. Let me check the arithmetic out loud: 134 plus 7 plus 5 equals 146, which is the number of rows I read, so every row is accounted for. The five flagged rows are the ones with empty dates I saw in Calc. I did not delete them, because a missing date is a question to ask the client."

### Cells 12 and 13: save results
Markdown: "Step 6, Save the results. This cell writes the clean rows to expenses underscore clean dot csv and the flagged rows to expenses underscore flagged dot csv, each with a header line."
```
## Step 6: Save the results
This cell writes the clean rows to expenses_clean.csv and the flagged rows to expenses_flagged.csv, each with a header line.
```
Code, say each line: "for path, comma, data, in, two pairs in parentheses: CLEAN with clean, and FLAGGED with flagged. Colon. Indented: with open, path, comma, quote w quote, comma, newline equals two quotes, as f, colon. Indented again: writer equals csv dot DictWriter, f, comma, fieldnames equals FIELDS. Then writer dot writeheader. Then writer dot writerows, data. Shift and Tab back, then: print, quote Wrote, comma, CLEAN, comma, quote and, comma, FLAGGED."
```python
for path, data in ((CLEAN, clean), (FLAGGED, flagged)):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(data)
print("Wrote", CLEAN, "and", FLAGGED)
```
"I will press Shift and Enter. The output says Wrote expenses clean dot csv and expenses flagged dot csv. In the Explorer panel on the left, two new files appeared under deliverables. I can see expenses underscore clean dot csv and expenses underscore flagged dot csv."

### Cells 14 and 15: totals
Markdown: "Step 7, Total spend per category. This cell adds up the amount for each category in the clean data and prints totals from highest to lowest. The top category is the first one to review for savings."
```
## Step 7: Total spend per category
This cell adds up the amount for each category in the clean data and prints totals from highest to lowest. The top category is the first one to review for savings.
```
Code, say each line: "totals equals Counter, open and close parentheses. for row in clean, colon. Indented: totals, open square bracket, row of category, close square bracket, plus equals, float, open parenthesis, row of amount, close parenthesis. Shift and Tab. for category, comma, total, in, totals dot most underscore common, open and close parentheses, colon. Indented: print, open parenthesis, f, quote, open curly brace category, close curly brace, colon, space, open curly brace total, colon, dot 2 f, close curly brace, quote, close parenthesis."
```python
totals = Counter()
for row in clean:
    totals[row["category"]] += float(row["amount"])
for category, total in totals.most_common():
    print(f"{category}: {total:.2f}")
```
"I will press Shift and Enter. The output lists the totals from highest to lowest: Office Supplies, seventeen thousand two hundred seventy-three dollars and nine cents. Travel, fourteen thousand ninety dollars and twenty-five cents. Utilities, nine thousand seven hundred sixty dollars and sixty-four cents. Meals, nine thousand one hundred thirty-two eighty-four. Marketing, nine thousand eighteen fifty-eight. Software, six thousand seven hundred forty-three zero two. Office Supplies is the largest cost, so that is where I will focus my recommendation."

### Save and close
"The notebook is complete, with fifteen cells: seven text cells, seven code cells, and the title. I will save it by pressing the Command key and the S key together on the keyboard."
[Press Cmd+S. Hold 1 second.]
"Saved. The dot on the notebook tab is gone. Now I will close VS Code by clicking the red circle at the top left corner of its window."
[Click red. Hold 1 second.]
"VS Code is closed."

## PART 4. Terminal: verify the output files (lookup) [about 15:30 to 18:30]
"My fourth step is to verify the files from the command line. I will open Terminal."
"I will click the Terminal icon in the Dock, a black square with a greater-than sign, because Terminal lets me list files and count lines independently of the notebook."
[Click. Hold 1 second.]
"Terminal opened in a window in the middle of the screen. The prompt shows a neutral user name, not a personal name. The window is small enough that I can still see the Dock and the menu bar clock."
"First I will move into my deliverables folder. I will type: c, d, space, Desktop, slash, deliverables. Then I will press the Enter key to run it."
[Type cd Desktop/deliverables. Press Enter. Hold 1 second.]
"I pressed Enter. Terminal printed nothing, which is normal for the change directory command. The prompt now ends with the word deliverables, so I am in the right folder."
"Next I will list the files. I will type: l, s, and press Enter."
[Type ls. Press Enter. Hold 1 second.]
"I pressed Enter. The Terminal printed four names: expense underscore audit dot i p y n b, expenses underscore clean dot csv, expenses underscore flagged dot csv, and input. This confirms my notebook and both output files exist."
"Now I will count the lines in the clean file. I will type: w, c, space, dash, l, space, expenses, underscore, clean, dot, csv. Then press Enter."
[Type wc -l expenses_clean.csv. Press Enter. Hold 1 second.]
"I pressed Enter. The Terminal printed 135 followed by the file name. That means the file has 135 lines: 134 data rows plus 1 header line. This matches the 134 rows kept in my notebook."
"I will do the same check for the flagged file. I will type: w c space dash l space expenses underscore flagged dot csv, and press Enter."
[Type wc -l expenses_flagged.csv. Press Enter. Hold 1 second.]
"The Terminal printed 6, which is 5 flagged rows plus the header. This also matches the notebook."
"I will close Terminal by clicking the red circle at the top left of its window."
[Click red. If a prompt appears: "A prompt asked to close the running process. I will click Terminate, because I am finished with it."]
"Terminal is closed."

## PART 5. LibreOffice Calc: build the summary workbook (create, then lookup) [about 18:30 to 24:00]
"My fifth step is to build a summary workbook. I will open LibreOffice from the Dock."
[Click the LibreOffice icon. Hold 1 second.]
"In the Start Center I will click Open File, in the left column, because I want to open the clean CSV."
[Click. Hold 1 second.]
"In the dialog, I will click Desktop in the left sidebar. Then I will double-click the folder deliverables. Then I will double-click the file expenses underscore clean dot csv."
[Click, double-click, double-click, 1 second after each.]
"In the Text Import window, the Comma separator is checked, so I will click OK at the bottom right."
[Click. Hold 1 second.]
"The clean data opened. It has 135 rows including the header. I will click cell A1, the top left cell, because I want to select all the data to build a pivot table."
[Click. Hold 1 second.]
"I will press the Command key and the A key together on the keyboard to select all cells. The data is highlighted."
[Press Cmd+A. Hold 1 second.]
"Now I will click the Insert menu in the menu bar at the top of the screen, because the Pivot Table command is there."
[Click Insert. Hold 1 second.]
"I will move down to Pivot Table and click it. A submenu appeared, and I will click Insert or Edit Pivot Table."
[Click, click. Hold 1 second.]
"A small window asks for the data source. Current selection is chosen, which is what I want. I will click OK."
[Click. Hold 1 second.]
"The Pivot Table Layout window opened. On the right side, under Available Fields, I see four boxes: date, vendor, amount, and category."
"I will press and hold the mouse button on the box called category, drag it to the box called Row Fields on the left, and release. I am doing this because I want one row for each category."
[Drag. Release. Hold 1 second.]
"Category is now in Row Fields. Next I will drag the box called amount into the box called Data Fields, because I want the total amount for each category."
[Drag. Release. Hold 1 second.]
"Amount appears in Data Fields as Sum, amount. That is the total I want. I will click OK at the bottom of this window."
[Click. Hold 1 second.]
"A new sheet appeared with the pivot table. Column A lists the six categories, column B shows each total, and the last row is Total Result."
"The Office Supplies total here is seventeen thousand two hundred seventy-three dollars and nine cents. This matches the notebook output."
"Next I will add a chart. I will click on the first category cell, then hold the mouse and drag down to the last category total in column B, so I select the categories and totals but not the Total Result row."
[Drag. Release. Hold 1 second.]
"I will click the Insert menu again and click Chart."
[Click, click. Hold 1 second.]
"The Chart Wizard opened. On the left is a list of chart types. I will click Bar, because a bar chart makes it easy to compare categories."
[Click Bar. Hold 1 second.]
"A preview shows six bars. I will click the Finish button at the bottom of the wizard."
[Click Finish. Hold 1 second.]
"The chart appeared on the sheet. Office Supplies has the tallest bar, then Travel, then Utilities. To leave chart editing, I will click on an empty cell far from the chart."
[Click. Hold 1 second.]

### Check formula (lookup)
"Now I will verify the pivot total with a separate formula. I will click an empty cell to the right of the pivot table, cell D one."
[Click. Hold 1 second.]
"I will type: equals, SUM, open parenthesis. Then I will click the tab at the bottom of the window called expenses underscore clean, to switch sheets."
[Type =SUM(. Click the sheet tab. Hold 1 second.]
"I will click the header letter C at the top of column C, which selects the whole amount column. Then I will type a close parenthesis and press Enter."
[Click C. Type ). Press Enter. Hold 1 second.]
"I pressed Enter. The result is the sum of every amount in the clean data. I will compare it to the Total Result in the pivot table. They match, so the pivot table did not lose or double-count any row."

### Save the workbook
"I will click File in the menu bar, then click Save As."
[Click, click. Hold 1 second.]
"In the Name box, I will type: expense, underscore, summary."
[Type. Hold 1 second.]
"Below it, I will open the file type dropdown and choose ODF Spreadsheet, dot o d s."
[Click dropdown. Choose ODS. Hold 1 second.]
"In the left sidebar, I will click Desktop, then double-click the folder deliverables, so the file is saved there. Then I will click Save."
[Click, double-click, click Save. Hold 1 second.]
"If a prompt asks about the file format, I will click Use ODF Format."
[Click if shown.]
"The workbook is saved as expense underscore summary dot o d s. I will close Calc by clicking the red circle at the top left."
[Click red. Hold 1 second.]
"If the Start Center is still open, I will close it with its red circle too."

## PART 6. VS Code: write the audit notes (create) [about 24:00 to 26:00]
"My sixth step is to write the audit notes. I will click the VS Code icon in the Dock."
[Click. Hold 1 second.]
"VS Code reopened with the deliverables folder. In the Explorer panel, at the top right next to the folder name, I will click the New File icon, because I want a new Markdown file."
[Click. Hold 1 second.]
"I will type: audit, underscore, notes, dot, m, d, and press Enter."
[Type audit_notes.md. Press Enter. Hold 1 second.]
"An empty file opened. I will type four lines, saying each aloud before I type it."
"Line one: pound sign, space, Audit Notes."
"Line two: Top categories, colon, Office Supplies 17,273.09, comma, Travel 14,090.25, comma, Utilities 9,760.64."
"Line three: Issues fixed, colon, 7 duplicate rows removed, comma, 5 rows flagged for a missing date, comma, and 10 category spelling variants merged."
"Line four: Recommendation, colon, review Office Supplies spending, the largest category, for possible savings."
```
# Audit Notes
Top categories: Office Supplies 17,273.09, Travel 14,090.25, Utilities 9,760.64.
Issues fixed: 7 duplicate rows removed, 5 rows flagged for a missing date, and 10 category spelling variants merged.
Recommendation: review Office Supplies spending, the largest category, for possible savings.
```
"I will press Command and S to save. Then I will click the red circle at the top left to close VS Code."
[Cmd+S. Click red. Hold 1 second each.]
(If you used AI to prepare any text before recording, state that in the metadata Request or Task Description, not in the video. Do not use AI while recording.)

## PART 7. Finder: show the deliverables (lookup) [about 26:00 to 27:30]
"My last step is to show my deliverables. I will click the Finder icon at the far left of the Dock."
[Click. Hold 1 second.]
"In the sidebar I will click Desktop, then double-click the folder deliverables."
[Click, double-click. Hold 1 second.]
"The folder contains six items. I will move my mouse over each one as I name it."
"One, the input folder, which holds expenses underscore raw dot c s v, my original starting file."
"Two, expense underscore audit dot i p y n b, the notebook with all my cleaning code and explanations."
"Three, expenses underscore clean dot csv, with 134 clean rows."
"Four, expenses underscore flagged dot csv, with the 5 transactions that have no date."
"Five, expense underscore summary dot o d s, the workbook with the pivot table and bar chart."
"Six, audit underscore notes dot m d, my short written report."
[Mouse rests on the folder. Do not close Finder. Begin the epilogue.]

## PART 8. Epilogue (3 to 4 minutes, never more than 4) [about 27:30 to 31:00]
Stay on the open deliverables folder. Speak at a calm, steady pace. Do not say you are stopping the recording; simply finish the last sentence.

"This is my epilogue, where I summarize how I did the task and how I checked it.

My goal was to take a messy yearly expense CSV, clean it, and produce a category summary with a chart and a short audit report. I started with one input file of about one hundred and forty-six made-up transactions. I finished with a clean data file, a flagged file, a summary workbook with a pivot table and a bar chart, and a written audit note. All of them are here in the deliverables folder on the Desktop.

First, how I verified the result. In the notebook, the counts add up: seven duplicates, five missing dates, and one hundred and thirty-four clean rows make one hundred and forty-six, which is exactly how many rows I started with. In Terminal, the clean file had one hundred and thirty-five lines, which is the rows plus one header line, and the flagged file had six lines, which is five rows plus the header. In LibreOffice Calc, a separate SUM formula over the clean amounts matched the Total Result in the pivot table, so no money was lost or counted twice. And the category check showed exactly six clean names instead of the many spelling variants I saw at the start.

Second, my approach. I looked at the raw data in Calc first, because a bookkeeper should see the problems before writing any code. I then used a notebook, because each step can be run and checked on its own, and a reviewer can read the explanation above every code cell. The order of the steps matters. I normalized the text before removing duplicates, because two rows that differ only by capital letters or a trailing space would otherwise slip through as different rows. I also flagged the rows with missing dates instead of deleting them, because a missing date is a question to ask the client, not a reason to throw away a real expense.

Third, the challenges. The hardest judgment was deciding what counts as a duplicate. Two real purchases can be identical, for example two coffees at the same cafe on the same day. I matched on date, vendor, amount, and category together, which is strict enough to avoid removing real purchases, but a human should still review the seven removed rows before filing taxes. Another challenge was trust. A pivot table can look right and still be wrong, so I checked the totals two different ways: the notebook output and a separate formula in Calc.

Fourth, the quality of the work. The output files have clear header lines and consistent category names, so anyone can open them in any spreadsheet program. The notebook has a text explanation above each code cell, so the logic can be followed without reading every line of code. The summary workbook has one chart that answers one question: where does the money go. If I had more time, I would add matching for similar vendor names, such as Corner Cafe and Corner Café, and a monthly breakdown so seasonal spending would be visible.

Finally, my reflection. This workflow mirrors real small-business bookkeeping before tax filing: inspect the data, clean it, summarize it, verify it, and write a short recommendation. The biggest category, Office Supplies, is the first place I would look for savings. The key lesson is that cleaning data is not just fixing formats. It is making decisions about what to keep, what to remove, and what to ask about, and then proving that the numbers still add up. Thank you for watching."

---

## Review-feedback coverage (self-check before submitting)
- Opening under 20 seconds, using the exact template, and the description minimized. Done in Part 0.
- Every click named (what, where, why), including red close buttons and Don't Save. Done throughout.
- Cursor held still 1 second after each click. Marked in brackets.
- No PII: tasker user, neutral Mac name, made-up data. Checklist at top.
- Dock, clock with seconds, Accessibility Inspector visible; each app closed before the next opens.
- Commands and results narrated: "I typed ... I pressed Enter. The Terminal printed ... which means ...".
- Starting material shown first (input folder) and included in deliverables. Part 1 and Part 7.
- Deliverables folder on the Desktop, narrated at the end, then epilogue of 4 minutes or less, no "stop recording" sentence.
- Metadata: Request equals the goal sentence; one numbered step list; topology on one line:
  Finder (LOOKUP) -> LibreOffice Calc (LOOKUP) -> Visual Studio Code* (CREATE) -> Terminal.app (LOOKUP) -> LibreOffice Calc (CREATE) -> LibreOffice Calc (LOOKUP) -> Visual Studio Code (CREATE) -> Finder (LOOKUP)
