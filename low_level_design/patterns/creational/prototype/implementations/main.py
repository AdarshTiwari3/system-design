"""client"""

from registry import PrototypeRegistry
from document import Document

def run_prototype_creation():

    #Create prototype of Document type as we will clone document object
    resume_template=Document("Resume","\nName:\nJohn Doe", {"type": "resume", "version": 1.0})
    report_template=Document("Report","Summary:\nDetails:",{"type":"report", "version":2.0})

    #register them in prototype registry
    registry=PrototypeRegistry()
    registry.register("resume",resume_template)
    registry.register("report", report_template)

    #clone from documents

    new_resume=registry.clone("resume")
    
    new_resume.set_title("John Snow's Resume")
    new_resume.set_metadata({"type": "resume", "version": 1.1})


    # Print both to verify independence
    print("--- Original Resume Template ---")
    print(resume_template)

    print("\n--- Cloned & Customized Resume ---")
    print(new_resume)
        
if __name__ == "__main__":
    print("\nPrototype Design Pattern")
    run_prototype_creation()