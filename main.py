import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class Employeedetails(App):
    def build(self):
        self.title="APMS A.S.PETA EMPLOYEE DETAILS"

        layout=GridLayout(cols=2,rows=13,row_force_default=True,row_default_height=45,spacing=5,padding=10)

        #head_label=Label(text="EMPLOYEE DETAILS",font_size=20,bold=True,height=10)

        name=Label(text="FULL NAME",font_size=20,bold=True,height=5)
        self.name_input=TextInput(multiline=False,font_size=25)
        
        qualification=Label(text="QUALIFICATION",font_size=20,bold=True,height=5)
        self.qu_input=TextInput(multiline=False,font_size=25)

        designation=Label(text="DESIGNATION",font_size=20,bold=True,height=5)
        self.d_input=TextInput(multiline=False,font_size=25)

        doj=Label(text="DATE OF JOINING",font_size=20,bold=True,height=5)
        self.doj_input=TextInput(multiline=False,font_size=25)

        hrmsid=Label(text="HRMS ID",font_size=20,bold=True,height=5)
        self.hrms_input=TextInput(multiline=False,font_size=25)

        cfmsid=Label(text="CFMS ID",font_size=20,bold=True,height=5)
        self.cfms_input=TextInput(multiline=False,font_size=25)

        aadhar=Label(text="AADHAR NO",font_size=20,bold=True,height=5)
        self.aadhar_input=TextInput(multiline=False,font_size=25)

        pan=Label(text="PAN",font_size=20,bold=True,height=5)
        self.pan_input=TextInput(multiline=False,font_size=25)

        voterid=Label(text="VOTER ID",font_size=20,bold=True,height=5)
        self.voter_input=TextInput(multiline=False,font_size=25)

        phoneno=Label(text="PHONE NO",font_size=20,bold=True,height=5)
        self.phone_input=TextInput(multiline=False,font_size=25)


        mailid=Label(text="MAIL ID",font_size=20,bold=True,height=5)
        self.mail_input=TextInput(multiline=False,font_size=25)

        
        submit_button=Button(text="SUBMIT",font_size=20,on_press=self.SUBMIT)


        
        #layout.add_widget(head_label)

        layout.add_widget(name)
        layout.add_widget(self.name_input)

        layout.add_widget(qualification)
        layout.add_widget(self.qu_input)

        layout.add_widget(designation)
        layout.add_widget(self.d_input)

        layout.add_widget(doj)
        layout.add_widget(self.doj_input)

        layout.add_widget(hrmsid)
        layout.add_widget(self.hrms_input)

        layout.add_widget(cfmsid)
        layout.add_widget(self.cfms_input)

        layout.add_widget(aadhar)
        layout.add_widget(self.aadhar_input)

        layout.add_widget(pan)
        layout.add_widget(self.pan_input)

        layout.add_widget(voterid)
        layout.add_widget(self.voter_input)

        layout.add_widget(phoneno)
        layout.add_widget(self.phone_input)

        layout.add_widget(mailid)
        layout.add_widget(self.mail_input)

        layout.add_widget(submit_button)



        return layout
    
    def SUBMIT(self,instance):
        name=self.name_input.text
        qualification=self.qu_input.text
        designation=self.d_input.text
        doj=self.doj_input.text
        hrmsid=self.hrms_input.text
        cfmsid=self.cfms_input.text
        aadhar=self.aadhar_input.text
        pan=self.pan_input.text
        voterid=self.voter_input.text
        phoneno=self.phone_input.text
        mailid=self.mail_input.text
        

        if name.strip()=='' or qualification.strip()=='' or designation.strip()=='' or doj.strip()=='' or hrmsid.strip()=='' or cfmsid.strip()=='' or aadhar.strip()=='' or pan.strip()=='' or voterid.strip()=='' or phoneno.strip()==''  or mailid.strip()=='':
            
            message="please fill in all fields"

        else:
            filename = name+'.txt'
            with open(filename, 'w') as file:
                file.write('name: {}\n'.format(name))
                file.write('qualification: {}\n'.format(qualification))
                file.write('designation: {}\n'.format(designation))

                file.write('doj: {}\n'.format(doj))

                file.write('hrmsid: {}\n'.format(hrmsid))

                file.write('cfmsid: {}\n'.format(cfmsid))

                file.write('aadhar: {}\n'.format(aadhar))

                file.write('pan: {}\n'.format(pan))

                file.write('voterid: {}\n'.format(voterid))

                file.write('phoneno: {}\n'.format(phoneno))

                file.write('mailid: {}\n'.format(mailid))

            message="SUBMISSION SUCCESSFUL"    


         
        popup=Popup(title="SUBMIT STATUS", content=Label(text=message),size_hint=(None,None), size=(400, 200))
        popup.open()


        
        









 

    


if __name__=='__main__':
   Employeedetails().run()
