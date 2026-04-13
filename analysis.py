import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# LOAD DATASET 
df=pd.read_csv("data.csv")
print("📊 Original Dataset:\n",df)
# FEATURE 1: TOTAL&AVERAGE
df["Total"]=df[["Maths","English","Science","Computer","German"]].sum(axis=1)
df["Average"]=df["Total"]/3
# FEATURE 2: GRADE SYSTEM
def assign_grade(avg):
    if avg>=90:
        return "A+"
    elif avg>= 75:
        return "A"
    elif avg>=60:
        return "B"
    elif avg>=40:
        return "C"
    else:
        return "Fail"
df["Grade"]=df["Average"].apply(assign_grade)
# FEATURE 3: Pass/ Fail
df["Result"]=df["Average"].apply(lambda x:"Pass" if x>=40 else "Fail")
# FEATURE 4: TOPPER 
top_student= df.loc[df["Total"].idxmax()]
print("\n🏆 Overall Topper:\n", top_student)
#FEATURE5: SUBJECT WISE TOPPER 
print("\n📚 Subject Wise Topper:")
for subject in ["Maths","English","Science","Computer","German"]:
    topper=df.loc[df[subject].idxmax()]
    print(f"{subject} Topper:{topper['Name']}({topper[subject]})")
# FEATURE6: CLASS INSIGHTS 
print("\n📊  Class Insight:")
print("Average Marks:\n",df[["Maths","Science","English","Computer","German"]].mean())
pass_percentage=(df["Result"]=="Pass").mean()*100
print(f"Pass Percentage:{pass_percentage:.2f}%")
#FEATURE 7: HIGHLIGHT WEAK STUDENTS 
weak = df[df["Average"] < 70]
print("\n⚠️ Students needing Improvement:\n", weak["Name"])
#FEATURE 8: BEST SUBJECT OVERALL

#FEATURE 9: SORTING 
df_sorted= df.sort_values(by="Total",ascending=False)
print("\n📈 Students Ranked:\n", df_sorted[["Name","Total","Grade"]])
#FEATURE 10: Top 3 STUDENTS 
top3 = df.sort_values(by="Total", ascending=False).head(3)
print("\n🏆 Top 3 Students:\n", top3[["Name","Total"]])
#FEATURE 11: PERFORMANCE CATEGORY
def performance(avg):
    if avg >= 80:
        return "Excellent"
    elif avg >= 60:
        return "Good"
    else:
        return "Needs Improvement"

df["Performance"] = df["Average"].apply(performance)
#FEATURE 12 : VISUALIZATION 
#BAR CHART 
df.plot(x="Name",y=["Maths","Science","English","Computer","German"],kind="bar")
plt.title("Subject Wise Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# PIE CHART FOR RESULTS 
df["Result"].value_counts().plot(kind="pie",autopct='%1.1f%%')
plt.title("Pass vs Fail Distribution ")
plt.ylabel("")
plt.show()
#CORRELATION HEATMAP
plt.figure(figsize=(6,4))
sns.heatmap(df[["Maths","Science","English","Computer","German","Total"]].corr(),annot=True,cmap="coolwarm")
plt.title("Correlation heatmap")
plt.show()
#DISTRIBUTION PLOT
sns.histplot(df["Total"],bins=5,kde=True)
plt.title("Distribution of Total Marks")
plt.show()
# FEATURE :13 SAVE OUTPUT 
df.to_csv("Updated_data.csv",index=False)
print("\n Updated dataset saved as 'Updated_data.csv")






