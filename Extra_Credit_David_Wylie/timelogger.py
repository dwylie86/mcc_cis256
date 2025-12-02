# David Wylie
# CIS256 Term (Fall 2025)
# Extra Credit Assignment
# timelogger.py - decorator for logging function timing


import time


def timelog(filename):
    """
    Allows us to decorate functions to time them and save to a file
    params: filename to save the log statements to
    """
    def timer(func):
        """
        A decorator to calculate how long a function runs.

        Parameters
        ----------
        func: callable
        The function being decorated.

        Returns
        -------
        func: callable
        The decorated function.
        """

        def wrapper(*args, **kwargs):
            # Start the timer
            start = time.time()
            # Call the `func`
            result = func(*args, **kwargs)
            # End the timer
            end = time.time()

            with open(filename, 'a') as f:
                f.write(
                    f"{func.__name__} took {round(end - start, 4)} "
                    "seconds to run!\n"
                    )
            return result

        return wrapper

    return timer


if __name__ == "__main__":
    @timelog('testtimer.txt')
    def waste_time(number_reps):
        """
        Test function for timelog decorator
        params: number of reps the number of times the function will run
        """
        for i in range(1, number_reps):
            print(f"This is {i}")
            time.sleep(1)

    # now we call the wrapped function
    waste_time(10)
