
'''
Flight Entertainment

This is a program that tells whether, given movie lengths and flight time,
if there are exactly two movies that are equal to the total flight time.

'''

'''
 is_flight_length_movies_present

 This function takes in a list of movie lenghts
 present in-flight and the total flight time.
 It return True/False based on if there are
 two movies whose total run time equals flight time.

 @input:
	m_length (list) : list of movies present in flight entertainment system
	f_length (int) : flight length

 @Returns: If there are two movies within m_lengths whose sum equals total flight length
'''
def is_flight_length_movies_present(m_lengths, f_length):
    m_lengths.sort()
    movies_present = False
    left = 0
    right = len(m_lengths) - 1

    while(left < right):
        if (m_lengths[left] + m_lengths[right] > f_length):
            right -= 1
        elif (m_lengths[left] + m_lengths[right] < f_length):
            left += 1
        else:
            return True
    return False


def run_test(m_length, f_length):
    print "\n========================"
    print "Testing data\n m_length : {0}\n f_length : {1}".format(m_length, f_length)
    print "Two movies present ? => {0}".format(is_flight_length_movies_present(movie_lengths, flight_length))
    print "========================\n"

movie_lengths = [30, 50, 10, 80, 10, 120, 60]
flight_length = 180

run_test(movie_lengths, flight_length) # 120 + 60 = 180 => True

movie_lengths = [60, 120, 10, 80, 10, 9, 70]
flight_length = 180

run_test(movie_lengths, flight_length) # 120 + 60 = 180 => True

movie_lengths = [30,20]
flight_length = 180

run_test(movie_lengths, flight_length) # 30 + 20 = 50 => False


movie_lengths = [180]
flight_length = 180

run_test(movie_lengths, flight_length) # 180 = 180 => False because user has to watch exactly two movies


movie_lengths = []
flight_length = 180

run_test(movie_lengths, flight_length) # empty list => False because this flight aint got no movies
