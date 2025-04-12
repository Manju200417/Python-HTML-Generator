def make_html(h1,par):  #with color property code  Version => 1.1
  
  # Use default content if user didn't input anything
  if not h1:
      h1 = "<h1>Default Heading</h1>"
  if not par:
      par = "<p>Default Paragraph</p>"
    
  return f'''<html>
    <body>
        {h1}
        {par}
    </body>
</html>'''

def ask_user(): #This function is used to ask user for heading and paragraph
     print("Welcome to HTML Generator")
     hed =''
     parac =''
     while True:
      ch = int(input("1.Heading \n2.Paragraph \n3.Give Me Html file\n Enter your choice => "))
      match ch:
        case 1:
          hed = heading()
        case 2:
          parac = para()
        case 3:
         return make_html(hed,parac)
        case _:
          print("Invalid Choice Try Again")

def heading():  #This function is used to create a heading with optional color styling
  content = input("Enter Heading content :")
  h1 = f'<h1>{content}</h1>'
  ch = int(input("Do you want to add color to Heading => 1.Yes 2.No :"))
  match ch:
      case 1:
       color = input("Enter a color : ")
       with_color = f' style ="color:{color}"'
       h1 = f'<h1{with_color}>{content}</h1>'
       return h1
      case 2:
        return h1
      case _:
        print("Invalid Choice Try Again")

def para(): #This function is used to create a paragraph with optional color property
  content = input("Enter paragraph content :")
  para = f'<p>{content}</p>'
  ch = int(input("Do you want to add color to paragraph => 1.Yes 2.No :"))
  match ch:
      case 1:
       color = input("Enter a color : ")
       with_color = f' style ="color:{color}"'
       para = f'<p{with_color}>{content}</p>'
       return para
      case 2:
        return para
      case _:
        print("Invalid Choice Try Again")

data = ask_user()

with open('index.html','w') as file:
   file.write(data)
   print("HTML file Successfully Created...")