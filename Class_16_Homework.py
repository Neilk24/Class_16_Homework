def shutdown():
        x=input('Did you finish your homework? ')

        if x=='yes':
                y=input('Did you finish your food? ')

                if y=='yes':
                        z=input('Did you finish your 30 mins of reading? ')

                        if z=='yes':
                                i=input('Did you finish your extracurricular activities? ')

                                if i=='yes':
                                        j=input('Did you finish your science olympiad material? ')

                                        if j=='yes':
                                                n=input('Do you want to shutdown your computer? ')

                                                if n=='yes':
                                                        print("Shutting down.....")
                                                else:
                                                        print('Shutdown Aborted.')

                                        elif j=='no':
                                                print('Shutdown Aborted. Please finish all of your work and then try again.')
                                        else:
                                                print('Sorry, please try again.')  
                                                
                                elif i=='no':
                                        print('Shutdown Aborted. Please finish all of your work and then try again.')
                                else:
                                       print('Sorry, please try again.')

                        elif z=='no':
                                print('Shutdown Aborted. Please finish all of your work and then try again.')
                        else:
                                print('Sorry, please try again.')

                elif y=='no':
                        print('Shutdown Aborted. Please finish all of your work and then try again.')
                else:
                        print('Sorry, please try again.') 

        elif x=='no':
                print('Shutdown Aborted. Please finish all of your work and then try again.')
        else:
                print('Sorry, please try again.')

shutdown()