'''Check site availability'''

#  from Lesson_4.website_alive.make_request import make_request_
from website_alive.check_response import check_response_


def main():
    '''Run check_response function
        from website_alive package with user input'''

    url = input("Enter the link: ")
    if check_response_(url):
        print("Site is alive!")
    else:
        print("Site is down :(")


if __name__ == '__main__':
    main()
