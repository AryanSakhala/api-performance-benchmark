# Recording Script: Exact vs Approximate Math Benchmark (end to end, about 28 minutes)

Lines in quotes are spoken aloud, word for word. Lines in [brackets] are actions: do them, do not say them. Announce every action BEFORE you do it (what, where, why), do it, hold the mouse still 1 second, then describe the result. Nothing is copy-pasted or cloned: every file is created live. Type the code yourself while looking at the script.

Replace the Part 0 opening with the exact template in the Writer Guidelines. It must finish within 20 seconds including minimizing the description.

## Before recording (do not narrate)
- Log in as your tasker macOS user, neutral Mac name, no personal name anywhere.
- Clock shows seconds. Dock visible. Accessibility Inspector pinned to the Dock and running.
- Desktop empty: NO deliverables folder yet. Only the task description document open.
- Resize each app window to about the middle 60% of the screen, never full screen, so no window covers another for more than 30 seconds. Close each app before opening the next.
- No restricted apps, no TextEdit, no AI while recording, nothing pasted.
- Typing must stay at 35% of the video or less. Rehearse the typing time. Fallback if too long: leave out the softmax block (the `def softmax` function and the `for size` loop).
- Silences under 45 seconds. Your timings will differ from the sample numbers in this script: always read your own numbers aloud.

## Narration pattern for EVERY action
WHAT ("I will click / double-click / press ...") + WHERE ("... at the top left / in the Dock ...") + WHY ("... because ..."). [Move slowly, click, hold 1 second.] RESULT ("I clicked it. Now ... is showing / the Terminal printed ..., which means ...").

---

## PART 0. Opening (15 to 18 seconds)
[Task description fills the screen. Mouse rests in the middle.]
"Hello. In this task I am a machine learning engineer. My goal is to benchmark exact and approximate versions of exp, sigmoid, and softmax in Python across different input values and sizes, and measure speed and absolute error, to identify the accuracy versus speed trade-off. I will use Visual Studio Code, Terminal, LibreOffice Calc, and Finder. Now I will minimize this task description."
"I will move my mouse to the top left corner of this window, where there are three small colored circles, and click the yellow one, the minimize button, because I want a clear screen."
[Click yellow. Hold 1 second.]
"I clicked it, and the description is minimized into the Dock."

## PART 1. Visual Studio Code: create the folder and write the benchmark (CREATE)
"My first step is to create my project folder and write the benchmark script. I will click the VS Code icon, the blue ribbon-shaped icon, in the Dock at the bottom of the screen, because I will write my code there."
[Click. Hold 1 second.]
"VS Code opened in a window, not full screen. I can still see the clock at the top and the Dock at the bottom."
"I will click File in the menu bar at the very top of the screen, because Open Folder is under it."
[Click File. Hold 1 second.]
"I will click Open Folder."
[Click. Hold 1 second.]
"A file dialog opened. In the sidebar on the left I will click Desktop, because I want my new folder on the Desktop."
[Click. Hold 1 second.]
"The Desktop is empty. I will click the New Folder button at the bottom left of the dialog, because I need to create my project folder."
[Click. Hold 1 second.]
"A box asks for the folder name. I will type: d, e, l, i, v, e, r, a, b, l, e, s, and click Create."
[Type deliverables. Click Create. Hold 1 second.]
"The folder deliverables is created on the Desktop and is selected. I will click the Open button at the bottom right, because I want to work inside it."
[Click Open. Hold 1 second.]
"If a prompt asks whether I trust the authors, I will click Yes, I trust the authors, because I just created this folder. [If none appears: No prompt appeared, so I continue.]"
[Click if shown. Hold 1 second.]
"The Explorer panel on the left shows the folder deliverables, and it is empty. I will click the New File icon, the small page with a plus sign, at the top right of the Explorer panel."
[Hover until the label shows. Click. Hold 1 second.]
"I will type: benchmark, dot, p, y, and press Enter."
[Type benchmark.py. Enter. Hold 1 second.]
"The file benchmark dot p y is created and open in the editor on the right."
"Before I type, here is the plan. The script compares exact and approximate versions of three functions. For exp, I compare the exact math dot exp against a six-term Taylor series approximation. For sigmoid, I compare the exact formula against a fast approximation. For softmax, which turns a list of numbers into probabilities, I compare a version built on exact exp against one built on the Taylor exp. For each, I measure speed in nanoseconds per call and absolute error compared with the exact answer, and write everything to a CSV file."
"I will now type the script line by line, saying what each line does. If VS Code adds an extra closing bracket or quote, I will press Delete. After an indented block I will press Shift and Tab to move back left."

L1: "I will type: import, csv, comma, math, comma, time. These modules write CSV files, provide math functions, and measure time."
```python
import csv, math, time
```
"Enter twice for a blank line."
L3: "I will define the Taylor approximation. I type: def, taylor underscore exp, open parenthesis, x, close parenthesis, colon. This function approximates e to the power x using a short series. Enter."
```python
def taylor_exp(x):
```
L4: "Indented: term, equals, total, equals, 1.0. Both start at one. Enter."
```python
    term = total = 1.0
```
L5: "for, k, in, range, open parenthesis, 1, comma, 7, close parenthesis, colon. This adds six terms. Enter."
```python
    for k in range(1, 7):
```
L6: "term, times equals, x, divided by, k. Each new term is the previous one times x over k. Enter."
```python
        term *= x / k
```
L7: "total, plus equals, term. Then Enter and Shift and Tab."
```python
        total += term
```
L8: "return, total. Enter twice."
```python
    return total
```
L10: "Now softmax. def, softmax, open parenthesis, values, comma, exp, close parenthesis, colon. It takes a list of numbers and the exp function to use. Enter."
```python
def softmax(values, exp):
```
L11: "top, equals, max, open parenthesis, values, close parenthesis. I subtract the largest value first, which is the standard trick that keeps numbers stable. Enter."
```python
    top = max(values)
```
L12: "parts, equals, an open square bracket, exp, open parenthesis, v, minus, top, close parenthesis, for, v, in, values, a close square bracket. Enter."
```python
    parts = [exp(v - top) for v in values]
```
L13: "total, equals, sum, open parenthesis, parts, close parenthesis. Enter."
```python
    total = sum(parts)
```
L14: "return, an open square bracket, p, divided by, total, for, p, in, parts, a close square bracket. This divides each part by the total so they add up to one. Enter twice and Shift and Tab."
```python
    return [p / total for p in parts]
```
L16: "Now the sigmoid functions. sigmoid, equals, lambda, x, colon, 1, divided by, an open parenthesis, 1, plus, math dot exp, open parenthesis, minus x, close parenthesis, close parenthesis. This is the exact sigmoid. Enter."
```python
sigmoid = lambda x: 1 / (1 + math.exp(-x))
```
L17: "fast underscore sigmoid, equals, lambda, x, colon, 0.5, plus, x, divided by, an open parenthesis, 2, times, an open parenthesis, 1, plus, abs, open parenthesis, x, close parenthesis, close parenthesis, close parenthesis. This is a cheap approximation with no exp inside. Enter twice."
```python
fast_sigmoid = lambda x: 0.5 + x / (2 * (1 + abs(x)))
```
L19: "Now a list of the four methods to compare. methods, equals, an open square bracket. Enter. Each entry says: the function name, the method name, the function to time, and the exact function to compare against."
```python
methods = [
```
L20: "Indented: an open parenthesis, quote exp quote, comma, quote exact quote, comma, math dot exp, comma, math dot exp, close parenthesis, comma. Enter."
```python
    ("exp", "exact", math.exp, math.exp),
```
L21: "Next: quote exp quote, quote taylor quote, taylor underscore exp, math dot exp. Enter."
```python
    ("exp", "taylor", taylor_exp, math.exp),
```
L22: "quote sigmoid quote, quote exact quote, sigmoid, sigmoid. Enter."
```python
    ("sigmoid", "exact", sigmoid, sigmoid),
```
L23: "quote sigmoid quote, quote fast quote, fast underscore sigmoid, sigmoid. Enter, then Shift and Tab."
```python
    ("sigmoid", "fast", fast_sigmoid, sigmoid),
```
L24: "A close square bracket. Enter twice."
```python
]
```
L26: "rows, equals, an empty list. This will hold all measurements. Enter."
```python
rows = []
```
L27: "for, func, comma, method, comma, approx, comma, exact, in, methods, colon. This loops over the four methods. Enter."
```python
for func, method, approx, exact in methods:
```
L28: "for, x, in, an open parenthesis, minus 6, comma, minus 2, comma, 0, comma, 2, comma, 6, close parenthesis, colon. These are my five test inputs. Enter."
```python
    for x in (-6, -2, 0, 2, 6):
```
L29: "start, equals, time dot perf underscore counter, open and close parentheses. This reads a precise clock. Enter."
```python
        start = time.perf_counter()
```
L30: "for, underscore, in, range, open parenthesis, 100000, close parenthesis, colon. I repeat the call one hundred thousand times to get a stable time. Enter."
```python
        for _ in range(100000):
```
L31: "approx, open parenthesis, x, close parenthesis. Enter, then Shift and Tab."
```python
            approx(x)
```
L32: "ns, equals, an open parenthesis, time dot perf underscore counter, open and close parentheses, minus, start, close parenthesis, divided by, 100000, times, 1e9. This converts total seconds into nanoseconds per call. Enter."
```python
        ns = (time.perf_counter() - start) / 100000 * 1e9
```
L33: "rows, dot, append, open parenthesis, an open square bracket, func, comma, method, comma, x, comma, round of ns and 1, comma, abs of approx of x minus exact of x, a close square bracket, a close parenthesis. The last value is the absolute error. Then Enter twice and Shift and Tab twice."
```python
        rows.append([func, method, x, round(ns, 1), abs(approx(x) - exact(x))])
```
L35: "Now softmax. for, size, in, an open parenthesis, 10, comma, 100, comma, 1000, close parenthesis, colon. These are the vector sizes. Enter."
```python
for size in (10, 100, 1000):
```
L36: "values, equals, an open square bracket, an open parenthesis, i, percent sign, 13, close parenthesis, minus 6, for, i, in, range, open parenthesis, size, close parenthesis, a close square bracket. This builds a list of numbers between minus 6 and 6. Enter."
```python
    values = [(i % 13) - 6 for i in range(size)]
```
L37: "reference, equals, softmax, open parenthesis, values, comma, math dot exp, close parenthesis. This is the exact answer to compare against. Enter."
```python
    reference = softmax(values, math.exp)
```
L38: "for, method, comma, exp, in, an open parenthesis, an open parenthesis, quote exact quote, comma, math dot exp, close parenthesis, comma, an open parenthesis, quote taylor quote, comma, taylor underscore exp, close parenthesis, close parenthesis, colon. Enter."
```python
    for method, exp in (("exact", math.exp), ("taylor", taylor_exp)):
```
L39: "start, equals, time dot perf underscore counter, open and close parentheses. Enter."
```python
        start = time.perf_counter()
```
L40: "for, underscore, in, range, open parenthesis, 200, close parenthesis, colon. Two hundred repeats is enough for a whole vector. Enter."
```python
        for _ in range(200):
```
L41: "result, equals, softmax, open parenthesis, values, comma, exp, close parenthesis. Enter, then Shift and Tab."
```python
            result = softmax(values, exp)
```
L42: "ns, equals, an open parenthesis, time dot perf underscore counter, open and close parentheses, minus, start, close parenthesis, divided by, 200, times, 1e9. Enter."
```python
        ns = (time.perf_counter() - start) / 200 * 1e9
```
L43: "error, equals, max, open parenthesis, abs, open parenthesis, a, minus, b, close parenthesis, for, a, comma, b, in, zip, open parenthesis, result, comma, reference, close parenthesis, close parenthesis. This is the largest difference from the exact softmax. Enter."
```python
        error = max(abs(a - b) for a, b in zip(result, reference))
```
L44: "rows, dot, append, open parenthesis, an open square bracket, quote softmax quote, comma, method, comma, size, comma, round of ns and 1, comma, error, a close square bracket, a close parenthesis. Enter twice and Shift and Tab twice."
```python
        rows.append(["softmax", method, size, round(ns, 1), error])
```
L46: "Now I save the file. with, open, open parenthesis, quote benchmark underscore results dot csv, quote, comma, quote w quote, comma, newline equals two quotes, close parenthesis, as, f, colon. Enter."
```python
with open("benchmark_results.csv", "w", newline="") as f:
```
L47: "writer, equals, csv dot writer, open parenthesis, f, close parenthesis. Enter."
```python
    writer = csv.writer(f)
```
L48: "writer dot writerow, an open parenthesis, a list of five quoted names: function, method, input, ns underscore per underscore call, abs underscore error, close parenthesis. Enter."
```python
    writer.writerow(["function", "method", "input", "ns_per_call", "abs_error"])
```
L49: "writer dot writerows, open parenthesis, rows, close parenthesis. Then Enter twice and Shift and Tab."
```python
    writer.writerows(rows)
```
L51: "Finally: print, open parenthesis, len of rows, comma, quote measurements written, quote, close parenthesis."
```python
print(len(rows), "measurements written")
```
"The script is complete. I will press the Command key and the S key together to save it."
[Cmd+S. Hold 1 second.]
"Saved. The dot on the tab is gone. In summary, the script times four methods at five inputs, times two softmax versions at three sizes, and records the speed and error of each. That is twenty plus six, so twenty-six measurements."
"I will close VS Code by clicking the red circle at the top left of its window."
[Click red. Hold 1 second.]

## PART 2. Terminal: run the benchmark and check the CSV (CREATE)
"My second step is to run the benchmark. I will click the Terminal icon in the Dock, the black square with a greater-than sign, because Terminal runs my Python script."
[Click. Hold 1 second.]
"Terminal opened in a window in the middle of the screen with a neutral user name. I can still see the clock and the Dock."
"I will type: c, d, space, Desktop, slash, deliverables, and press Enter, to move into my folder."
[Type cd Desktop/deliverables. Enter. Hold 1 second.]
"I pressed Enter. Nothing printed, which is normal. The prompt now ends with deliverables."
"I will type: l, s, and press Enter, to list the files."
[Type ls. Enter. Hold 1 second.]
"The Terminal printed one file: benchmark dot p y, my script."
"I will run it. I will type: python3, space, benchmark dot p y, and press Enter. It runs about a hundred thousand calls per test, so it may take a few seconds. I will wait quietly and keep the mouse still."
[Type python3 benchmark.py. Enter. Wait for it. Hold still.]
"I pressed Enter and waited. The Terminal printed: 26 measurements written. That means the script ran without errors, and 26 is twenty speed tests for exp and sigmoid plus six for softmax."
"I will list the files again. I will type l s and press Enter."
[Type ls. Enter. Hold 1 second.]
"The Terminal now prints two files: benchmark underscore results dot csv and benchmark dot p y. My script created the CSV."
"I will count the lines. I will type: w, c, space, dash, l, space, benchmark underscore results dot csv, and press Enter."
[Type wc -l benchmark_results.csv. Enter. Hold 1 second.]
"The Terminal printed 27, followed by the file name. That is 26 measurements plus 1 header line, which matches the printed message."
"I will close Terminal by clicking the red circle at the top left. If a prompt appears, I will click Terminate."
[Click red. Hold 1 second.]

## PART 3. LibreOffice Calc: inspect the measurements (LOOKUP)
"My third step is to inspect the results in a spreadsheet. I will click the LibreOffice icon in the Dock, the white and green document icon."
[Click. Hold 1 second.]
"In the Start Center I will click Open File, in the left column."
[Click. Hold 1 second.]
"In the dialog I will click Desktop in the sidebar, double-click the folder deliverables, then double-click benchmark underscore results dot csv."
[Click, double-click, double-click. Hold 1 second each.]
"The Text Import window appeared. Comma is checked, which is correct, so I will click OK at the bottom right."
[Click OK. Hold 1 second.]
"The file opened. Column A is the function, B is the method, C is the input value or the vector size, D is the time in nanoseconds per call, and E is the absolute error. Row 1 is the header and rows 2 to 27 are my 26 measurements."
"I want to find where the approximations fail, so I will sort by error. I will click cell E1, the header of the abs error column, because that is the column I will sort on."
[Click E1. Hold 1 second.]
"I will click the Data menu at the top of the screen, then click Sort Descending, or Sort, and choose abs underscore error with Descending."
[Click Data. Click Sort. In the dialog choose abs_error, Descending. Click OK. Hold 1 second each.]
"The table is sorted with the largest errors on top. The top row is exp, taylor, input 6, with an error of about 158.8. The next is exp, taylor, input minus 6, with an error of about 31. After those, softmax taylor with 10 values has an error of about 0.63. This tells me the Taylor exp breaks badly far from zero."
"I will scroll down with two fingers on the trackpad to see the smaller errors."
[Scroll slowly.]
"Further down, sigmoid fast has errors up to about 0.069, and every exact method has an error of exactly zero, because I compare it against itself."
"Next, speed. I will click cell D1 and sort again, but I will look at it rather than sort: the exact exp costs only tens of nanoseconds, while the Taylor exp costs more than three hundred. So the approximation is slower, not faster, in Python."

## PART 4. LibreOffice Calc: pivot table, chart, and save (CREATE)
"Now I will summarize with a pivot table. I will click cell A1, the top left cell."
[Click A1. Hold 1 second.]
"I will hold Shift and click cell E27, to select all the data from A1 to E27."
[Shift-click E27. Hold 1 second.]
"I will click the Insert menu, then Pivot Table, then Insert or Edit Pivot Table."
[Click, click, click. Hold 1 second each.]
"Current selection is chosen, so I will click OK."
[Click OK. Hold 1 second.]
"The Pivot Table Layout window opened. I will drag function into the Row Fields box, and then drag method into the Row Fields box under it, so each row is one function and one method."
[Drag function. Drag method. Hold 1 second.]
"I will drag ns underscore per underscore call into the Data Fields box. By default it says Sum. I will double-click it, choose Average from the list, and click OK in that small window, because I want the average time, not the total."
[Drag. Double-click. Select Average. Click OK. Hold 1 second.]
"Now I will drag abs underscore error into the Data Fields box, double-click it, choose Max, and click OK, because I want the worst error."
[Drag. Double-click. Select Max. Click OK. Hold 1 second.]
"The layout shows Average of ns per call and Max of abs error. I will click OK at the bottom of the layout window."
[Click OK. Hold 1 second.]
"A new sheet appeared. It lists six rows, one for each function and method. For example: exp exact averages about 85 nanoseconds with a max error of 0. Exp taylor averages about 336 nanoseconds with a max error of about 158.8. Sigmoid exact is about 126, sigmoid fast is about 90 with a max error of 0.069. Softmax exact is about 34,900, and softmax taylor is about 138,400 with a max error of about 0.63. Your numbers may differ slightly, and I will read them from my screen."
"Now I will add a chart. I will select the method names and the average time column, by clicking the first method cell and dragging to the last average time cell."
[Drag. Release. Hold 1 second.]
"I will click the Insert menu, then click Chart."
[Click, click. Hold 1 second.]
"In the Chart Wizard, I will click Bar in the list on the left, because a bar chart compares categories."
[Click Bar. Hold 1 second.]
"I will click Finish at the bottom."
[Click Finish. Hold 1 second.]
"The bar chart appeared. The softmax bars are much taller than the others, because softmax processes whole lists of numbers instead of a single value. Among single-number functions, the Taylor exp bar is the tallest, and the fast sigmoid bar is shorter than the exact sigmoid bar."
"To leave chart editing, I will click an empty cell far from the chart."
[Click. Hold 1 second.]
"I will click File, then Save As."
[Click, click. Hold 1 second.]
"In the Name box I will type: benchmark, underscore, summary."
[Type. Hold 1 second.]
"I will make sure the type says ODF Spreadsheet, dot o d s. In the sidebar I will click Desktop, double-click deliverables, and click Save. If a prompt asks about the format, I will click Use ODF Format."
[Narrate each click. Hold 1 second each.]
"The workbook is saved as benchmark underscore summary dot o d s. I will close Calc by clicking the red circle at the top left, and close the Start Center the same way if it stays open."
[Click red. Hold 1 second.]

## PART 5. Visual Studio Code: write the report (MODIFY)
"My fifth step is to write the analysis report. I will click the VS Code icon in the Dock."
[Click. Hold 1 second.]
"VS Code reopened with the deliverables folder. The Explorer panel shows benchmark dot p y and the CSV."
"I will click the New File icon at the top right of the Explorer panel, type: benchmark, underscore, report, dot, m, d, and press Enter."
[Click. Type. Enter. Hold 1 second.]
"An empty file opened. I will type a short report, saying each line before I type it. I will use my own numbers from the pivot table. The numbers below are sample values."
"Line one: pound sign, space, Benchmark Report."
"Line two: Speed colon, the exact exp averages about 85 nanoseconds, the Taylor exp about 336, which is about four times slower. The fast sigmoid is about 90 versus about 126 for the exact sigmoid."
"Line three: Accuracy colon, the Taylor exp has a max error of about 158.8 at x equals 6, the fast sigmoid has a max error of 0.069, and the Taylor softmax has an error of 0.63 at 10 values."
"Line four: Recommendation colon, in Python the exact math dot exp is both faster and exact, so use the fast sigmoid only where an error of 0.07 is acceptable, and avoid the Taylor exp outside minus 2 to 2."
```
# Benchmark Report
Speed: exact exp averages about 85 ns, Taylor exp about 336 ns (about 4x slower). Fast sigmoid is about 90 ns versus about 126 ns for exact sigmoid.
Accuracy: Taylor exp has a max error of about 158.8 at x = 6, fast sigmoid 0.069, and Taylor softmax 0.63 at 10 values.
Recommendation: in Python the exact math.exp is both faster and exact. Use the fast sigmoid only where an error of 0.07 is acceptable, and avoid the Taylor exp outside -2 to 2.
```
"I will press Command and S to save, then click the red circle at the top left to close VS Code."
[Cmd+S. Click red. Hold 1 second each.]

## PART 6. Terminal: confirm every file exists (LOOKUP)
"My sixth step is to confirm my files. I will click the Terminal icon in the Dock."
[Click. Hold 1 second.]
"I will type: c d space Desktop slash deliverables, press Enter, then type l s and press Enter."
[Type each. Enter. Hold 1 second.]
"The Terminal printed four files: benchmark dot p y, benchmark underscore report dot m d, benchmark underscore results dot csv, and benchmark underscore summary dot o d s. All four deliverables exist."
"I will close Terminal with the red circle at the top left."
[Click red. Hold 1 second.]

## PART 7. Finder: show the deliverables (LOOKUP)
"My last step is to show the folder. I will click the Finder icon at the far left of the Dock."
[Click. Hold 1 second.]
"In the sidebar I will click Desktop, then double-click the folder deliverables."
[Click, double-click. Hold 1 second.]
"The folder contains four files. I will move the mouse over each as I name it."
"One, benchmark dot p y, the Python script that times and compares the methods."
"Two, benchmark underscore results dot csv, the 26 measurements."
"Three, benchmark underscore summary dot o d s, the workbook with the pivot table and the bar chart."
"Four, benchmark underscore report dot m d, my written analysis and recommendation."
[Mouse rests on the folder. Do not close Finder. Begin the epilogue.]

## PART 8. Epilogue (3 to 4 minutes, never more than 4)
Stay on the open deliverables folder. Speak calmly. Do not say you are stopping the recording. Just finish the last sentence. Use your own numbers if they differ.

"This is my epilogue, where I summarize how I did the task and how I checked it.

My goal was to find out whether faster approximations of exp, sigmoid, and softmax are worth the accuracy they give up. I wrote a Python benchmark that times an exact and an approximate version of each, measures the absolute error against the exact answer, and records everything in a CSV. I then sorted and summarized the data in LibreOffice Calc, built a pivot table and a chart, and wrote a report with a recommendation. All files are in this deliverables folder on the Desktop.

First, how I verified the work. In Terminal, the script printed twenty-six measurements written, and the CSV had twenty-seven lines, which is twenty-six rows plus the header. The exact methods showed an error of exactly zero, which is a sanity check, because each is compared with itself. I also checked that the errors made sense: the Taylor series is accurate near zero and fails far from it, which is how a six-term series should behave.

Second, my approach. I measured speed by repeating each call a hundred thousand times and dividing, because a single call is too fast to time reliably. For softmax I used whole vectors of ten, one hundred, and one thousand numbers, and compared against the exact softmax. I used the standard trick of subtracting the largest value first, so the numbers stay stable.

Third, what the results show. The surprise is that, in pure Python, the approximations are mostly not faster. The exact math dot exp is compiled code and takes about eighty-five nanoseconds, while my Taylor version, written in Python, takes about three hundred and thirty-six, around four times slower, and its error reaches about one hundred and fifty-nine at x equals six. The Taylor softmax is also about four times slower. The fast sigmoid is the one real win. It is about thirty percent faster than the exact sigmoid, with a maximum error of about seven hundredths. So the accuracy versus speed trade-off only pays off when the approximation is cheaper than the native function.

Fourth, challenges and quality. The main challenge was fair timing: the same repeat count, the same inputs, and the exact result as the reference. Timings also vary a little between runs, so I treat differences of a few percent as noise. The files are simple, the chart compares methods at a glance, and the report states the recommendation in plain words. With more time, I would use NumPy to compare vectorized versions, add more inputs, and repeat the runs to get an error bar on the timings.

Finally, a reflection. This is how an engineer decides whether an optimization is worth it: measure speed, measure error, and let the numbers decide. Here the answer is to keep the exact functions, and use the fast sigmoid only where an error of seven hundredths is acceptable. Thank you for watching."

---

## Review-feedback self-check (before you submit)
- Opening under 20 seconds with the exact template; description minimized.
- Every click narrated (what, where, why), including red close buttons and prompts; mouse still 1 second after each click.
- No personal info: tasker user, neutral Mac name.
- Dock, clock with seconds, Accessibility Inspector visible; no window full screen; no window covering another for more than 30 seconds.
- Commands and results narrated: "I typed ... I pressed Enter. The Terminal printed ..., which means ...".
- Starting material: none. No clone, no copy-paste, everything typed live.
- Every promised item shown: printed count, wc -l, error sort in Calc, pivot, chart, benchmark_summary.ods, benchmark_report.md, Finder tour.
- Epilogue 4 minutes or less; no "stop recording" sentence.
- Metadata: Request equals the TaskRecorder Goal exactly; one numbered list; topology: Visual Studio Code (CREATE) > Terminal.app (CREATE) > LibreOffice Calc (LOOKUP) > LibreOffice Calc (CREATE) > Visual Studio Code (MODIFY) > Terminal.app (LOOKUP) > Finder (LOOKUP).
