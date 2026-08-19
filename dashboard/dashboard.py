import os
import pandas as pd
import matplotlib.pyplot as plt

def load_data(cases_path="data/cases.csv", reviews_path="data/reviews.csv"):
    cases=pd.read_csv(cases_path)
    reviews=pd.read_csv(reviews_path) if os.path.exists(reviews_path) else pd.DataFrame()
    return cases,reviews

def summary(cases,reviews):
    n=len(reviews)
    accepted=int((reviews.human_decision=="Accepted").sum()) if n else 0
    return {"Total Cases":len(cases),"Reviewed":n,"Accepted":accepted,
            "Edited":int((reviews.human_decision=="Edited").sum()) if n else 0,
            "Rejected":int((reviews.human_decision=="Rejected").sum()) if n else 0,
            "AI-Human Agreement":accepted/n if n else 0}

def issue_chart(cases):
    ax=cases.concept.value_counts().plot(kind="bar",title="Cases by Issue Type")
    plt.tight_layout(); return ax.get_figure()

def severity_chart(cases):
    ax=cases.severity.value_counts().plot(kind="bar",title="Cases by Severity")
    plt.tight_layout(); return ax.get_figure()
