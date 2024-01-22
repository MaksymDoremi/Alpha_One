# Alpha 1
### Developer: Maksym Kintor C4b
### E-mail: `kintor@spsejecna.cz`
### Date: 21.12.2023

## Architecture:
<pre>
|___Alpha_One/
    |___README.md (this file)
    |___config/
        |______init__.py
        |___config.py
    |___src/
        |___package/
            |_____init__.py
            |___Evaluator.py
            |___Generator.py
            |___Subject.py
            |___Watchdog.py
        |___main.py (run project)
    |___tests/
        |___EvaluatorTest.py
        |___GeneratorTest.py
        |___SubjectTest.py
        |___WatchdogTest.py
        |___test.py (run tests)
    
</pre>

## Run Project
Navigate to folder `Alpha_One` with CMD.  
Run with `python src\main.py`

## Unit Test Project
Navigate to folder `Alpha_One` with CMD.  
Run with `python tests\test.py`

## Config file
Navigate to `Alpha_One\config\config.py`  
You are able to adjust:
- schedule - input schedule. Example [1,2,3,4,5...]
- subject_dcitionary - initial dictionary to decode schedule of numbers  
- process_count - initial value is YOUR cpu count - 1 watchdog ( as main )
- evaluator_process_count - math.floor(process_count / 4 * 3), equation which you can change
- generator_process_count - math.ceil(process_count / 4), equation which you can change
- timeout - initial timeout for the program to run is 180 seconds
- every_n_seconds - value in seconds, means that generator will each N seconds update shared list of schedules. Initial value is 2 seconds.
