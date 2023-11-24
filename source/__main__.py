from source.view.Page_principale.start_view import Start_view
 
if __name__ == "__main__":
    # Lancer la vue du menu démarrage
    current_view = Start_view()

    while current_view: 
        current_view.display()
        current_view = current_view.make_choice()    

         
"current_view = current_view.make_choice() pour passer à la vue suivante mais , pas cohérent avec notre implementation pour linsant"
  