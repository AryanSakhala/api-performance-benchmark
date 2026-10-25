# Recording Script: Loan Scenario Comparison (end to end, about 25 minutes)

Lines in quotes are spoken aloud, word for word. Lines in [brackets] are actions: do them, do not say them. Announce every action BEFORE you do it (what, where, why), do it, hold the mouse still for 1 second, then describe the result. Nothing is copy-pasted and nothing is cloned: every file is created live.

Replace the Part 0 opening with the exact template in the Writer Guidelines. It must finish within 20 seconds, including minimizing the description document.

## Before you press record (do not narrate)
- Log in as your dedicated tasker macOS user. Neutral Mac name, so no personal name shows anywhere.
- Menu bar clock shows seconds. Dock visible. Accessibility Inspector pinned to the Dock and running.
- Desktop is empty: NO deliverables folder yet. You create it on camera.
- Only the task description document is open. No restricted apps, no TextEdit, no AI tools while recording.
- Resize each app window to about the middle 60% of the screen, never full screen, so no window covers another, the Dock, or the Inspector for more than 30 seconds. Close each app before opening the next.
- Typing must stay at 35% of the video or less (script about 19 lines, report 5 lines). Silences must be under 45 seconds.
- Do not copy-paste anything. Type every line yourself.

## Narration pattern for EVERY action
1. WHAT: "I will click / double-click / right-click / press ..."
2. WHERE: "... at the top left / in the Dock / in the left sidebar ..."
3. WHY: "... because ..."
4. [Move the mouse slowly. Click. Hold still 1 second.]
5. RESULT: "I clicked it. Now ... is showing / the Terminal printed ..., which means ..."

---

## PART 0. Opening (15 to 18 seconds)
[Task description fills the screen. Mouse rests in the middle of the document.]
"Hello. In this task I am a loan analyst helping a small business owner compare mortgage options. My goal is to build and compare loan scenarios across different terms and interest rates, and measure the monthly payment and total interest, to identify the cheapest option. I will use Visual Studio Code, Terminal, LibreOffice Calc, and Finder. Now I will minimize this task description."
"I will move my mouse to the top left corner of this document window, where there are three small colored circles, and click the yellow one, the minimize button, because I want a clear screen."
[Move. Click yellow. Hold 1 second.]
"I clicked the yellow button, and the description is minimized into the Dock."

## PART 1. Visual Studio Code: create the folder and write the script (CREATE)
"My first step is to create my project folder and write a Python script. I will open Visual Studio Code, which I will call VS Code."
"I will move my mouse to the Dock at the bottom of the screen and click the VS Code icon, the blue ribbon-shaped icon, because I will write my code here."
[Click. Hold 1 second.]
"VS Code opened in a window, not full screen. I can still see the menu bar and clock at the top, and the Dock at the bottom."
"I need a folder for my work. I will click File in the menu bar at the very top of the screen, because the Open Folder command is under it."
[Click File. Hold 1 second.]
"The File menu opened. I will move down to Open Folder and click it."
[Click. Hold 1 second.]
"A file dialog opened. In the sidebar on the left, I will click Desktop, because I want the new folder to live on my Desktop."
[Click Desktop. Hold 1 second.]
"The Desktop is empty. At the bottom left of the dialog there is a button called New Folder. I will click it, because I need to create the folder."
[Click New Folder. Hold 1 second.]
"A box appeared asking for the folder name. I will type: d, e, l, i, v, e, r, a, b, l, e, s, and click the Create button."
[Type deliverables. Click Create. Hold 1 second.]
"I created a folder named deliverables on the Desktop. It is selected now. I will click the Open button at the bottom right of the dialog, because I want to work inside it."
[Click Open. Hold 1 second.]
"If a prompt asks whether I trust the authors, I will click Yes, I trust the authors, because I just created this folder. [If it does not appear, say: No prompt appeared, so I continue.]"
[Click if shown. Hold 1 second.]
"VS Code now shows the folder named deliverables in the Explorer panel on the left side, and it is empty."
"I will click the New File icon, the small page with a plus sign, at the top right of the Explorer panel, because I need to create my script file."
[Hover 1 second so the label shows, then click. Hold 1 second.]
"A text box appeared in the Explorer panel. I will type: loan, underscore, scenarios, dot, p, y. Then I will press the Enter key."
[Type loan_scenarios.py. Press Enter. Hold 1 second.]
"The file loan underscore scenarios dot p y is created and open in the large editor area on the right."
"Before I type, I will explain the plan. The script will calculate the monthly payment and the total interest for a loan of two hundred fifty thousand dollars, for four terms: ten, fifteen, twenty, and thirty years, at four interest rates: four and a half, five and a half, six and a half, and seven and a half percent. That makes sixteen scenarios. It will write them to a CSV file."
"I will now type the script line by line. After each line I will say what it does."
[VS Code may auto-indent and auto-close brackets and quotes. If it adds an extra closing character, press Delete. Press Shift+Tab to move left after a block.]

Line 1: "I will type: import, space, csv. This loads the module that writes CSV files."
```python
import csv
```
"I will press Enter twice to leave a blank line."
Line 3: "I will type: principal, space, equals, space, 250000. This is the loan amount in dollars."
```python
principal = 250000
```
Line 4: "Next: rows, equals, an open and close square bracket. This empty list will hold my results."
```python
rows = []
```
"Enter twice for a blank line."
Line 6: "Now the outer loop. I will type: for, space, years, space, in, space, an open parenthesis, 10, comma, 15, comma, 20, comma, 30, a close parenthesis, colon. This repeats the steps for each loan term. I press Enter, and VS Code indents the next line by four spaces."
```python
for years in (10, 15, 20, 30):
```
Line 7: "The inner loop: for, space, rate, space, in, an open parenthesis, 4.5, comma, 5.5, comma, 6.5, comma, 7.5, a close parenthesis, colon. This repeats for each interest rate, in percent. Enter."
```python
    for rate in (4.5, 5.5, 6.5, 7.5):
```
Line 8: "Now the monthly rate: r, equals, rate, divided by, 1200. Dividing by twelve months and by a hundred turns a yearly percent into a monthly decimal. Enter."
```python
        r = rate / 1200
```
Line 9: "The number of payments: n, equals, years, times, 12. Enter."
```python
        n = years * 12
```
Line 10: "The payment formula: payment, equals, principal, times, r, divided by, an open parenthesis, 1, minus, an open parenthesis, 1, plus, r, a close parenthesis, two asterisks, minus n, a close parenthesis. This is the standard formula for a fixed monthly loan payment. Enter."
```python
        payment = principal * r / (1 - (1 + r) ** -n)
```
Line 11: "I will save one result row: rows, dot, append, an open parenthesis, an open square bracket, years, comma, rate, comma, round of payment and 2, comma, round of payment times n minus principal and 2, a close square bracket, a close parenthesis. The last value is the total interest: all payments added up, minus the original loan."
```python
        rows.append([years, rate, round(payment, 2), round(payment * n - principal, 2)])
```
"I will press Enter twice, then press Shift and Tab to move back to the left edge."
Line 13: "Now I write the file. I will type: with, space, open, open parenthesis, quote, loan underscore scenarios dot csv, quote, comma, quote w quote, comma, newline equals two quotes, close parenthesis, as, f, colon. The w means write. Enter."
```python
with open("loan_scenarios.csv", "w", newline="") as f:
```
Line 14: "writer, equals, csv, dot, writer, open parenthesis, f, close parenthesis. Enter."
```python
    writer = csv.writer(f)
```
Line 15: "The header row: writer, dot, writerow, and a list of four quoted names: years, rate underscore percent, monthly underscore payment, total underscore interest. Enter."
```python
    writer.writerow(["years", "rate_percent", "monthly_payment", "total_interest"])
```
Line 16: "Now all my rows: writer, dot, writerows, open parenthesis, rows, close parenthesis. Then Enter twice and Shift and Tab."
```python
    writer.writerows(rows)
```
Line 18: "Finally a message so I can verify: print, open parenthesis, len of rows, comma, quote, scenarios written, quote, close parenthesis."
```python
print(len(rows), "scenarios written")
```
"The script is complete. I will press the Command key and the S key together to save it."
[Press Cmd+S. Hold 1 second.]
"Saved. The dot on the tab is gone. I will read the whole script one more time. It loops over four terms and four rates, computes the payment and total interest for each, and writes sixteen rows to a CSV."
"I will close VS Code by clicking the red circle at the top left of its window."
[Click red. Hold 1 second.]
"VS Code is closed."

## PART 2. Terminal: run the script and check the CSV (CREATE)
"My second step is to run the script. I will open Terminal. I will click the Terminal icon in the Dock, the black square with a greater-than sign, because Terminal runs my Python script."
[Click. Hold 1 second.]
"Terminal opened in a window in the middle of the screen. The prompt shows a neutral user name, and I can still see the menu bar clock and the Dock."
"I will move into my folder. I will type: c, d, space, Desktop, slash, deliverables, and press Enter."
[Type cd Desktop/deliverables. Enter. Hold 1 second.]
"I pressed Enter. Nothing was printed, which is normal. The prompt now ends with deliverables, so I am in the right folder."
"I will list the files to confirm. I will type: l, s, and press Enter."
[Type ls. Enter. Hold 1 second.]
"I pressed Enter. The Terminal printed one file: loan underscore scenarios dot p y. That is my script."
"Now I will run it. I will type: python3, space, loan underscore scenarios dot p y, and press Enter."
[Type python3 loan_scenarios.py. Enter. Hold 1 second.]
"I pressed Enter. The Terminal printed: 16 scenarios written. That means the script ran without errors, and 16 is four terms times four rates."
"I will list the files again. I will type l s and press Enter."
[Type ls. Enter. Hold 1 second.]
"The Terminal now prints two files: loan underscore scenarios dot csv and loan underscore scenarios dot p y. The CSV was created by my script."
"I will count its lines. I will type: w, c, space, dash, l, space, loan underscore scenarios dot csv, and press Enter."
[Type wc -l loan_scenarios.csv. Enter. Hold 1 second.]
"I pressed Enter. The Terminal printed 17, followed by the file name. That is 16 data rows plus 1 header line, which matches the 16 scenarios."
"I will close Terminal by clicking the red circle at the top left of its window. If a prompt appears, I will click Terminate."
[Click red. Hold 1 second.]

## PART 3. LibreOffice Calc: verify payments with PMT (LOOKUP)
"My third step is to check my Python results with an independent tool. I will open LibreOffice from the Dock, the white and green document icon, because Calc has a built-in payment function called PMT."
[Click. Hold 1 second.]
"The Start Center opened. I will click Open File, in the left column, because I want to open my CSV."
[Click. Hold 1 second.]
"In the dialog I will click Desktop in the sidebar, double-click the folder deliverables, then double-click loan underscore scenarios dot csv."
[Click, double-click, double-click, 1 second after each.]
"A Text Import window appeared. The Comma separator is checked, which is correct, so I will click OK at the bottom right."
[Click OK. Hold 1 second.]
"The file opened. Column A is years, B is rate percent, C is monthly payment, and D is total interest. Row 1 is the header, and rows 2 to 17 are my 16 scenarios."
"I will click cell E1, the first empty header cell to the right of column D, because I want to add a check column."
[Click E1. Hold 1 second.]
"I will type: PMT check, and press Tab. Then I will type: Difference, and press Enter."
[Type. Hold 1 second.]
"Now I will click cell E2, the first data row of the new column."
[Click E2. Hold 1 second.]
"I will type this formula: equals, minus, PMT, open parenthesis, B2, slash, 1200, semicolon, A2, times, 12, semicolon, 250000, close parenthesis. This calculates the monthly payment with Calc's own function, using the same rate, term, and loan amount. The minus sign makes the result positive. I press Tab."
[Type =-PMT(B2/1200;A2*12;250000). Press Tab. Hold 1 second.]
"I am now in F2. I will type: equals, ROUND, open parenthesis, E2, semicolon, 2, close parenthesis, minus, C2, and press Enter. This rounds the Calc payment to cents and subtracts my Python payment. A result of zero means they match."
[Type =ROUND(E2;2)-C2. Enter. Hold 1 second.]
"E2 shows two thousand five hundred ninety dollars and ninety-six cents, and F2 shows zero. The Calc result matches my script."
"To fill every row, I will click E2 and then hold Shift and click F17, to select the block from E2 to F17."
[Click E2. Shift-click F17. Hold 1 second.]
"I will press the Command key and the D key together, which fills the formulas down."
[Press Cmd+D. Hold 1 second.]
"I will scroll down with two fingers on the trackpad to check column F. All values in the Difference column are zero, or at most one cent from rounding. This confirms all sixteen Python payments are correct."
[Scroll slowly. Pause on the last rows.]

## PART 4. LibreOffice Calc: pivot table, chart, and save (CREATE)
"Next I will summarize total interest by term and rate. I will click cell A1, the top left cell, because I want to start my selection there."
[Click A1. Hold 1 second.]
"I will hold Shift and click cell D17, to select the data from A1 to D17. I am selecting only columns A to D, not the check columns."
[Shift-click D17. Hold 1 second.]
"I will click the Insert menu in the menu bar at the top of the screen, then click Pivot Table, then Insert or Edit Pivot Table."
[Click, click, click. Hold 1 second each.]
"A small window asks for the data source. Current selection is chosen, which is what I want. I will click OK."
[Click OK. Hold 1 second.]
"The Pivot Table Layout window opened. On the right, under Available Fields, I see years, rate underscore percent, monthly underscore payment, and total underscore interest."
"I will press and hold the mouse on years, drag it into the Row Fields box on the left, and release. This gives one row per loan term."
[Drag. Release. Hold 1 second.]
"I will drag rate underscore percent into the Column Fields box, at the top of the layout. This gives one column per interest rate."
[Drag. Release. Hold 1 second.]
"I will drag total underscore interest into the Data Fields box. It appears as Sum of total underscore interest, which is the cost I want to compare. I will click OK at the bottom."
[Drag. Release. Click OK. Hold 1 second.]
"A new sheet appeared. The rows are the four terms, the columns are the four rates, and each cell shows total interest. For example, ten years at four and a half percent shows sixty thousand nine hundred fifteen dollars and twenty-three cents. Thirty years at seven and a half percent shows three hundred seventy-nine thousand two hundred ninety-three dollars and six cents."
"I will now add a chart. I will click and drag across the pivot table, from the top left header to the last data cell, to select it, but not the Total Result row and column."
[Drag. Release. Hold 1 second.]
"I will click the Insert menu and click Chart."
[Click, click. Hold 1 second.]
"The Chart Wizard opened. In the list on the left, I will click Line, because a line chart shows how cost changes across terms."
[Click Line. Hold 1 second.]
"The preview shows four lines, one for each interest rate. I will click Finish at the bottom."
[Click Finish. Hold 1 second.]
"The line chart appeared. Each line rises as the term gets longer, and the seven and a half percent line is the highest."
"To leave chart editing, I will click an empty cell far from the chart."
[Click. Hold 1 second.]
"Now I will save the workbook. I will click File in the menu bar, then Save As."
[Click, click. Hold 1 second.]
"In the Name box I will type: loan, underscore, comparison."
[Type. Hold 1 second.]
"I will make sure the file type says ODF Spreadsheet, dot o d s. In the sidebar I will click Desktop, double-click the folder deliverables, and click Save. If a prompt asks about the format, I will click Use ODF Format."
[Narrate each click. Hold 1 second each.]
"The workbook is saved as loan underscore comparison dot o d s. I will close Calc by clicking the red circle at the top left. If the Start Center stays open, I will close it with its red circle too."
[Click red. Hold 1 second.]

## PART 5. Visual Studio Code: write the report (MODIFY)
"My fifth step is to write the analysis report. I will click the VS Code icon in the Dock."
[Click. Hold 1 second.]
"VS Code reopened with the deliverables folder. In the Explorer panel I can see my script, loan underscore scenarios dot p y, and the CSV."
"I will click the New File icon at the top right of the Explorer panel, because I want a Markdown report."
[Click. Hold 1 second.]
"I will type: loan, underscore, report, dot, m, d, and press Enter."
[Type loan_report.md. Enter. Hold 1 second.]
"An empty file opened. I will type five lines, saying each one before I type it."
"Line one: pound sign, space, Loan Report."
"Line two: Loan amount, colon, 250,000. Scenarios, colon, 4 terms of 10, 15, 20, and 30 years, times 4 rates of 4.5, 5.5, 6.5, and 7.5 percent."
"Line three: Cheapest overall, colon, 10 years at 4.5 percent, total interest 60,915.23, monthly payment 2,590.96."
"Line four: Most expensive overall, colon, 30 years at 7.5 percent, total interest 379,293.06, monthly payment 1,748.04."
"Line five: Trade-off, colon, the 30-year loan has the lowest monthly payment but costs far more in total interest. Recommendation, colon, choose the shortest term the monthly budget can support."
```
# Loan Report
Loan amount: 250,000. Scenarios: 4 terms (10, 15, 20, 30 years) x 4 rates (4.5%, 5.5%, 6.5%, 7.5%).
Cheapest overall: 10 years at 4.5%, total interest 60,915.23, monthly payment 2,590.96.
Most expensive overall: 30 years at 7.5%, total interest 379,293.06, monthly payment 1,748.04.
Trade-off: the 30-year loan has the lowest monthly payment but costs far more in total interest. Recommendation: choose the shortest term the monthly budget can support.
```
"I will press Command and S to save, then click the red circle at the top left to close VS Code."
[Cmd+S. Click red. Hold 1 second each.]

## PART 6. Terminal: confirm every file exists (LOOKUP)
"My sixth step is to confirm all my files exist. I will click the Terminal icon in the Dock."
[Click. Hold 1 second.]
"I will type: c d space Desktop slash deliverables, and press Enter. Then I will type l s and press Enter."
[Type each. Enter. Hold 1 second.]
"The Terminal printed four files: loan underscore comparison dot o d s, loan underscore report dot m d, loan underscore scenarios dot csv, and loan underscore scenarios dot p y. All four deliverables are present."
"I will close Terminal with the red circle at the top left."
[Click red. Hold 1 second.]

## PART 7. Finder: show the deliverables (LOOKUP)
"My last step is to show the folder. I will click the Finder icon at the far left of the Dock."
[Click. Hold 1 second.]
"In the sidebar I will click Desktop, then double-click the folder deliverables."
[Click, double-click. Hold 1 second.]
"The folder contains four files. I will move my mouse over each as I name it."
"One, loan underscore scenarios dot p y, the Python script that calculates the sixteen scenarios."
"Two, loan underscore scenarios dot csv, the results, with sixteen rows and a header."
"Three, loan underscore comparison dot o d s, the workbook with the PMT check, the pivot table, and the line chart."
"Four, loan underscore report dot m d, my written analysis and recommendation."
[Mouse rests on the folder. Do not close Finder. Begin the epilogue.]

## PART 8. Epilogue (3 to 4 minutes, never more than 4)
Stay on the open deliverables folder. Speak calmly. Do not say you are stopping the recording. Just finish the last sentence.

"This is my epilogue, where I summarize how I did the task and how I checked it.

My goal was to compare loan options for a small business owner. I built a Python script that calculates the monthly payment and total interest for a two hundred fifty thousand dollar loan across four terms and four interest rates, sixteen scenarios in total. I wrote the results to a CSV, checked them in LibreOffice Calc, summarized them with a pivot table and a line chart, and wrote a short report with a recommendation. Everything is in this deliverables folder on the Desktop.

First, how I verified the work. In Terminal, the script printed sixteen scenarios written, and the line count of the CSV was seventeen, which is sixteen rows plus the header. In Calc, I recomputed every payment with the built-in PMT function, a separate calculation from my Python formula, and the Difference column showed zero, or at most one cent of rounding. So two independent methods agree on all sixteen payments.

Second, my approach. I used a script rather than a manual calculation, because sixteen scenarios are easy to get wrong by hand, and a script can be re-run if the loan amount changes. I kept the program short and readable, with one loop for terms and one for rates. I used the standard fixed-payment loan formula, and I defined total interest as all payments added together, minus the original loan.

Third, what the numbers show, and the trade-off. A longer term lowers the monthly payment but increases total interest a lot. The cheapest option overall is ten years at four and a half percent, with about sixty thousand nine hundred fifteen dollars of interest, but its payment is the highest, at two thousand five hundred ninety-one dollars a month. The most expensive is thirty years at seven and a half percent, with about three hundred seventy-nine thousand dollars of interest, which is more than the loan itself. Rate matters too: at thirty years, moving from four and a half to seven and a half percent adds about one hundred seventy-three thousand dollars in interest.

Fourth, challenges and quality. The main challenge was getting the monthly rate right, because the formula needs the yearly percent divided by twelve months and by a hundred. A mistake there would make every number wrong, which is why I verified with PMT. The files are simple and open in any program. The chart answers one question, how cost grows with term and rate. With more time, I would add taxes, insurance, and extra payments, and compare scenarios against the owner's monthly budget.

Finally, a reflection. This is how an analyst turns a vague question, which loan should I take, into numbers that can be checked, charted, and explained. The recommendation is to choose the shortest term the monthly budget can support. Thank you for watching."

---

## Review-feedback self-check (before you submit)
- Opening under 20 seconds with the exact template; description minimized.
- Every click narrated (what, where, why), including red close buttons and prompts; mouse still for 1 second after each click.
- No personal info on screen or in audio: tasker user, neutral Mac name.
- Dock, clock with seconds, and Accessibility Inspector visible; windows not full screen; no window covering another for more than 30 seconds.
- Commands and results narrated: "I typed ... I pressed Enter. The Terminal printed ..., which means ...".
- Starting material: none, everything created from scratch and typed live. No clone, no copy-paste.
- All promised steps and deliverables shown: printed count, wc -l, PMT check, pivot table, chart, loan_comparison.ods, loan_report.md, Finder tour.
- Epilogue 4 minutes or less, no "stop recording" sentence.
- Metadata: Request equals the TaskRecorder Goal exactly (the Goal sentence from Part 0), one numbered step list, and this topology: Visual Studio Code (CREATE) > Terminal.app (CREATE) > LibreOffice Calc (LOOKUP) > LibreOffice Calc (CREATE) > Visual Studio Code (MODIFY) > Terminal.app (LOOKUP) > Finder (LOOKUP).
- The idea text says "line chart comparing payments across terms". The script builds the line chart from the pivot of total interest by term and rate. Reword the idea to say "a line chart comparing total interest across terms and rates" so the recording and the idea match exactly.
