def initialize():
    '''Initializes the global variables needed for the simulation.'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars

    global cur_star, cur_star_activity, tired

    cur_hedons = 0
    cur_health = 0

    cur_star = []
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = -1000

    tired = False


def star_can_be_taken(activity):
    '''Return True iff a star can be used to get more hedons for the activity.'''
    return activity == cur_star_activity and not bored_with_stars


def perform_activity(activity, duration):
    '''Simulate the performance of the activity for the duration.'''

    global cur_time, cur_health, cur_hedons, last_activity, tired, last_activity_duration, cur_star_activity

    if activity != 'resting' and activity != 'running' and activity != 'textbooks':
        return
    # updates the "game clock"
    cur_time += duration

    if activity == 'resting' and (
            duration >= 120 or (last_activity == 'resting' and last_activity_duration + duration >= 120)):
        tired = False

    cur_health += estimate_health_delta(activity, duration)
    cur_hedons += estimate_hedons_delta(activity, duration)

    cur_star_activity = None

    # updates info about the last activity
    if last_activity == activity:
        last_activity_duration += duration
    else:
        last_activity = activity
        last_activity_duration = duration

    if activity != 'resting':
        tired = True


def get_cur_hedons():
    '''Return the number of hedons the user has accumulated so far.'''
    return cur_hedons


def get_cur_health():
    '''Return the number of health points that the user has accumulated so far.'''
    return cur_health


def offer_star(activity):
    '''Simulate offering the user a star for engaging in the exercise activity'''
    global cur_star, cur_star_activity, bored_with_stars

    if activity != 'running' and activity != 'textbooks':
        return

    cur_star_activity = activity
    cur_star.append(cur_time)  # does this add the thing to the end of the list??????
    if len(cur_star) == 4:
        cur_star.remove(cur_star[0])
    if len(cur_star) == 3 and cur_time - cur_star[0] < 120:
        bored_with_stars = True


def most_fun_activity_minute():
    if estimate_hedons_delta('running', 1) > estimate_hedons_delta('textbooks', 1) and estimate_hedons_delta('running',
                                                                                                             1) > estimate_hedons_delta(
            'resting', 1):
        return 'running'
    if estimate_hedons_delta('textbooks', 1) > estimate_hedons_delta('resting', 1):
        return 'textbooks'
    return 'resting'


################################################################################
# These functions are not required, but we recommend that you use them anyway
# as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    if tired:
        return 0
    elif activity != last_activity:
        if activity == 'running':
            return 10
        if activity == 'textbooks':
            return 20
    else:
        if activity == 'running':
            return max([0, 10 - last_activity_duration])
        if activity == 'textbooks':
            return max([0, 20 - last_activity_duration])


def get_effective_minutes_left_health(activity):
    if last_activity == activity and activity == 'running':
        return max([0, 180 - last_activity_duration])
    if activity == 'running':
        return 180
    return


def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    if activity == 'resting':
        return 0
    hedons = 0
    if star_can_be_taken(activity):
        if duration >= 10:
            hedons += 30
        else:
            hedons += 3 * duration

    if tired:
        hedons -= 2 * duration
    elif activity == 'running':
        if duration <= 10:
            hedons += 2 * duration
        else:
            hedons += 2 * (20 - duration)
    elif activity == 'textbooks':
        if duration <= 20:
            hedons += duration
        else:
            hedons += 40 - duration

    return hedons


def estimate_health_delta(activity, duration):
    if activity == 'resting':
        return 0
    if activity == 'textbook':
        return 2 * duration
    if activity == 'running':
        if get_effective_minutes_left_health(activity) >= duration:
            return 3 * duration
        else:
            return 3 * get_effective_minutes_left_health(activity) + duration - get_effective_minutes_left_health(
                activity)
    if activity == 'textbooks':
        return 2 * duration

################################################################################

if __name__ == '__main__':
    initialize()