from calendar import HTMLCalendar
from Projects.models import Project




class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	
	def formatday(self, day, projects):
		projects_per_day = projects.filter(StartDate__day=day)
		d = ''
		for project in projects_per_day:
			d += f'<li> {project.Title}-{project.Description} </li>'
			

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	
	def formatweek(self, theweek, projects):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, projects)
		return f'<tr> {week} </tr>'

	
	def formatmonth(self, withyear=True):
		projects = Project.objects.filter(StartDate__year=self.year, StartDate__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, projects)}\n'
		return cal