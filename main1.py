import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition","Diseases"])




#Main Page
if(app_mode=="Home"):
    st.header("MULTIPLE LEAF DISEASE DETECTION SYSTEM")
    image_path = "home.jpg"
    st.image(image_path,use_column_width=True)
    st.markdown("""
    Welcome to the Multiple Leaf Disease Detection System! 🌿🔍
    
    Our mission is to help in identifying leaf diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

#About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into  different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing test images is created later for prediction purpose.
                 

                """)

#Prediction Page
elif(app_mode=="Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))

#diseases page
elif(app_mode=="Diseases"):
    st.sidebar.title("Remedies")
    app_mode2= st.sidebar.selectbox("Select Disease",["Common_rust","Black_rot","Powdery_mildew","Cercospora_leaf_spot","Northern_Leaf_Blight",
                                                      "Esca_(Black_Measles)","Leaf_blight_(Isariopsis_Leaf_Spot","Haunglongbing_(Citrus_greening)",
                                                      "Bacterial_spot","Early_blight","Late_blight","Leaf_scorch","Septoria_leaf_spot","Two-spotted_spider_mite",
                                                      "Target_Spot","Yellow_Leaf_Curl_Virus","mosaic_virus"])
    
    if(app_mode2=="Common_rust"):
        st.header("Common_rust")
        image_path = "common_rust.jpg"
        st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
Pustules: Small, raised blisters (pustules) appear on the leaves. These are initially cinnamon-brown in color.
                    
Leaf Discoloration: The area around the pustules may turn yellow, indicating chlorosis.
                    
Spore Spread: As the disease progresses, the pustules rupture, releasing powdery, orange-red spores that can spread to adjacent plants.
                    
Premature Leaf Senescence: Infected leaves may die prematurely, which can reduce photosynthetic capacity and weaken the plant.
   

                    
### fertilizers
Nitrogen (N): Moderate nitrogen levels are crucial as excessive nitrogen can increase susceptibility to rust. An application rate of around 80-120 kg/ha is recommended, adjusted based on the crop, soil fertility, and stage of growth.

Phosphorus (P) and Potassium (K): Phosphorus aids in root development and overall plant health. Typical applications are about 40-60 kg/ha. Potassium improves plant resistance to stress and diseases, including rust; about 100-150 kg/ha is advisable depending on soil test results.
                    
Calcium (Ca): Calcium strengthens plant cell walls, aiding in defense against pathogens. An application of 100-200 kg/ha can be beneficial, particularly in acidic soils needing liming.Magnesium (Mg): Magnesium is essential for photosynthesis and plant health. Apply around 20-30 kg/ha to ensure adequate magnesium levels.
                    
Micronutrients: Zinc (Zn) and manganese (Mn) are particularly important; zinc aids in plant hormone balance and manganese plays a role in photosynthesis and defense against fungal diseases. Apply around 5-10 kg/ha for manganese and 2-5 kg/ha for zinc.
                    

        
        """)
    elif(app_mode2=="Black_rot"):
        st.header("Black_rot")
        image_path = "black_rot.jpg"
        st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
                    
V-shaped or wedge-shaped yellowing: Leaves show yellow patches that typically start at the margins and move inward towards the veins, forming a V-shaped or wedge-shaped pattern.

Black veins: As the disease progresses, the veins within the yellow areas turn black.
                    
Lesions and Rotting: Small, dark lesions may appear on the leaves, stems, and sometimes on the fruit, leading to rotting if the infection is severe.

Stunted Growth and Wilting: Infected plants may exhibit stunted growth and wilting, especially under severe infection conditions.
                    
### fertilizers
Nitrogen (N): Maintain moderate levels, typically between 50 to 150 kg/ha (approximately 45 to 135 lbs/acre), applied in divided doses throughout the growing season based on soil test recommendations.
                    
Phosphorus (P) and Potassium (K): Apply about 50-100 kg/ha (45-90 lbs/acre) for phosphorus and 100-200 kg/ha (90-180 lbs/acre) for potassium, adjusted according to soil conditions to improve plant health and disease resistance.
                    
Calcium (Ca): Apply gypsum or calcium nitrate at about 500-1000 kg/ha (445-890 lbs/acre) to strengthen plant cell walls and decrease susceptibility to black rot, especially important in sandy soils.
                    
Micronutrients: Ensure plants have access to essential micronutrients through soil or foliar applications, adhering to specific crop needs and local soil conditions to help bolster plant defenses against diseases like black rot.
        
        """)

    elif(app_mode2=="Powdery_mildew"):
        st.header("Powdery_mildew")
        image_path = "powdery_mildew.jpg"
        st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
Leaf Spots: Small, circular to angular spots appear on the leaves, usually gray to tan in color, often with a darker border.

Chlorosis: Surrounding the spots, the leaf tissue may turn yellow, indicating chlorosis.
                    
Leaf Drop: As the disease progresses, infected leaves may yellow further, wither, and eventually drop off, which can reduce the overall photosynthetic area and weaken the plant.
                    
Defoliation: Severe infections can lead to significant defoliation, impacting crop yield and vigor.
                    
### fertilizers

Nitrogen (N): Use nitrogen cautiously as excessive amounts can increase susceptibility to the disease. Typically, an application rate of 50-80 kg/ha is recommended, adjusted based on the crop and soil nitrogen levels.

Phosphorus (P) and Potassium (K): Phosphorus supports root and overall plant health. Apply around 40-60 kg/ha. Potassium is important for enhancing disease resistance and overall plant health; recommended application is about 80-120 kg/ha based on soil test results.
                    
Calcium (Ca): Calcium helps strengthen cell walls and can aid in disease resistance. Application rates of 100-200 kg/ha are typical, depending on soil needs.
                    
Micronutrients: Ensure adequate levels of micronutrients, particularly manganese (Mn) and zinc (Zn), which are crucial for plant defense mechanisms. Typical application rates are around 5-10 kg/ha for manganese and 2-5 kg/ha for zinc.
        """)


    elif(app_mode2=="Cercospora_leaf_spot"):
        st.header("Cercospora_leaf_spot")
        image_path = "Cercospora_spot.jpg"
        st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
Leaf Spots: Small, circular to angular spots appear on the leaves, usually gray to tan in color, often with a darker border.

Chlorosis: Surrounding the spots, the leaf tissue may turn yellow, indicating chlorosis.
                    
Leaf Drop: As the disease progresses, infected leaves may yellow further, wither, and eventually drop off, which can reduce the overall photosynthetic area and weaken the plant.
                    
Defoliation: Severe infections can lead to significant defoliation, impacting crop yield and vigor.
                    
### fertilizers

Nitrogen (N): Use nitrogen cautiously as excessive amounts can increase susceptibility to the disease. Typically, an application rate of 50-80 kg/ha is recommended, adjusted based on the crop and soil nitrogen levels.

Phosphorus (P) and Potassium (K): Phosphorus supports root and overall plant health. Apply around 40-60 kg/ha. Potassium is important for enhancing disease resistance and overall plant health; recommended application is about 80-120 kg/ha based on soil test results.
                    
Calcium (Ca): Calcium helps strengthen cell walls and can aid in disease resistance. Application rates of 100-200 kg/ha are typical, depending on soil needs.
                    
Micronutrients: Ensure adequate levels of micronutrients, particularly manganese (Mn) and zinc (Zn), which are crucial for plant defense mechanisms. Typical application rates are around 5-10 kg/ha for manganese and 2-5 kg/ha for zinc.
        """)

    elif(app_mode2=="Northern_Leaf_Blight"):
        st.header("Northern_Leaf_Blight")
        image_path = "Northern_Leaf_Blight.jpg"
        st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
                    
Leaf Symptoms: Leaves exhibit "tiger-stripes" — irregular, chlorotic (yellow) patterns that often become necrotic (brown).

Vine Decline: Affected vines show signs of stunted growth and general decline.
                    
Fruit Symptoms: Berries develop dark spots, sometimes appearing sunken with cracks, resembling measles, which can render the fruit unusable.
                    
Wood Symptoms: The wood on infected vines shows black streaking and canker development when pruned or cut.

                    
### fertilizers
                    
Nitrogen (N): Apply nitrogen cautiously, as excessive nitrogen can exacerbate fungal diseases. A moderate application, typically around 40-70 kg/ha, can be sufficient, depending on the soil's natural fertility and vine requirements.

Phosphorus (P) and Potassium (K): Phosphorus should be applied at about 30-50 kg/ha to aid root development and plant vigor. Potassium is important for overall plant health and disease resistance; an application rate of 100-150 kg/ha is advisable, based on soil test results.
                    
Calcium (Ca): Calcium helps to strengthen cell walls and improve plant defenses against pathogens. Apply around 150-200 kg/ha of calcium, preferably in the form of gypsum if no pH adjustment is needed.
                    
Magnesium (Mg): Ensuring adequate magnesium is essential for photosynthesis and plant health. An application rate of 20-30 kg/ha can be beneficial.
                    
Micronutrients: Include essential micronutrients such as manganese (Mn), zinc (Zn), and boron (B), each typically applied at about 1-5 kg/ha. These help in various plant processes and can enhance resistance to stress.

        """)

    elif(app_mode2=="Esca_(Black_Measles)"):
        st.header("Esca_(Black_Measles)")
            #image_path = "home.jpg"
            #st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
Leaf Spots: Initially, small, irregularly shaped greyish spots appear on the leaves.

Lesion Growth: These spots can enlarge and coalesce, forming larger patches of dead tissue.
                    
Color Change: As the lesions age, they may turn from grey to brown or black, often surrounded by a chlorotic (yellow) halo.
                    
Leaf Drop: Severe infections can lead to premature leaf drop, affecting the photosynthetic capacity of the plant and potentially reducing yield.
                    
### fertilizers
Nitrogen (N): Provide moderate levels of nitrogen to avoid excessive vegetative growth which can be more susceptible to fungal infections. A typical application rate is 50-80 kg/ha, split into several applications during the growing season to prevent excessive growth spurts.

Phosphorus (P) and Potassium (K): Phosphorus aids in root development and overall plant health, and can be applied at a rate of 40-60 kg/ha. Potassium is crucial for disease resistance and overall plant strength; an application rate of 80-120 kg/ha is recommended based on soil test results.
                    
Calcium (Ca): Calcium strengthens cell walls and can help plants fend off pathogens. Application rates of about 150-200 kg/ha can be beneficial, particularly in the form of gypsum which does not alter soil pH.
                    
Micronutrients: Ensure a sufficient supply of essential micronutrients, particularly magnesium (Mg), which supports chlorophyll production and overall plant health. A recommended dose is around 20-30 kg/ha.

        """)

    elif(app_mode2=="Leaf_blight_(Isariopsis_Leaf_Spot"):
        st.header("Leaf_blight_(Isariopsis_Leaf_Spot)")
        image_path = "Leaf_blight_(Isariopsis_Leaf_Spot.jpg"
        st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
Leaf Spots: Initially, small, irregularly shaped greyish spots appear on the leaves.

Lesion Growth: These spots can enlarge and coalesce, forming larger patches of dead tissue.
                    
Color Change: As the lesions age, they may turn from grey to brown or black, often surrounded by a chlorotic (yellow) halo.
                    
Leaf Drop: Severe infections can lead to premature leaf drop, affecting the photosynthetic capacity of the plant and potentially reducing yield.
                    
### fertilizers
                    
Nitrogen (N): Provide moderate levels of nitrogen to avoid excessive vegetative growth which can be more susceptible to fungal infections. A typical application rate is 50-80 kg/ha, split into several applications during the growing season to prevent excessive growth spurts.

Phosphorus (P) and Potassium (K): Phosphorus aids in root development and overall plant health, and can be applied at a rate of 40-60 kg/ha. Potassium is crucial for disease resistance and overall plant strength; an application rate of 80-120 kg/ha is recommended based on soil test results.
                    
Calcium (Ca): Calcium strengthens cell walls and can help plants fend off pathogens. Application rates of about 150-200 kg/ha can be beneficial, particularly in the form of gypsum which does not alter soil pH.
                    
Micronutrients: Ensure a sufficient supply of essential micronutrients, particularly magnesium (Mg), which supports chlorophyll production and overall plant health. A recommended dose is around 20-30 kg/ha.
                    


        """)

    elif(app_mode2=="Bacterial_spot"):
        st.header("Bacterial_spot")
            #image_path = "home.jpg"
            #st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
Leaf Spots: Small, dark, water-soaked spots appear on the leaves. These spots may turn brown or black and can be surrounded by a yellow halo.

Fruit Lesions: On fruits, the spots start as small, raised, and greasy looking. They can develop into scabby or cracked areas that diminish the fruit's market value.
                    
Defoliation: Severe infections can lead to leaf drop as the spots coalesce and kill large areas of tissue.
                    
Wilting: Affected plants may exhibit signs of wilting and stunted growth, especially under high humidity and warm temperatures.
                    
### fertilizers
Nitrogen (N): Moderate nitrogen application is important as excessive nitrogen can lead to lush foliage that is more susceptible to diseases. An application rate of 80-100 kg/ha is recommended, depending on the crop and soil condition.

Phosphorus (P) and Potassium (K): Adequate phosphorus helps in root development and overall plant health. A typical application is about 50-70 kg/ha. Potassium is crucial for improving plant health and disease resistance; around 120-150 kg/ha is advisable, based on soil tests.
                    
Calcium (Ca): Calcium can strengthen plant cell walls, making them less susceptible to pathogen invasion. Apply around 100-200 kg/ha, depending on soil pH and existing calcium levels.
                    
Micronutrients: Ensuring sufficient levels of micronutrients like magnesium (Mg) and manganese (Mn) supports overall plant health. Application rates for magnesium are around 10-20 kg/ha and for manganese 5-10 kg/ha.

        """)

    elif(app_mode2=="Early_blight"):
        st.header("Early_blight")
            #image_path = "home.jpg"
            #st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
Concentric Rings: Infected leaves display brown spots with concentric rings that form a bullseye pattern.

Yellowing: The area around the spots can turn yellow.
                    
Leaf Drop: As the disease progresses, affected leaves may dry up and fall off, leading to significant defoliation.
                    
Stem and Fruit Lesions: The fungus can also infect stems and fruits, creating dark, sunken lesions on these parts.
                    
                    
### fertilizers
Nitrogen (N): Moderate nitrogen levels are crucial to avoid excessive leafy growth which is more susceptible to fungal attacks. A recommended application is about 80-100 kg/ha, depending on the specific crop and soil condition.

Phosphorus (P) and Potassium (K): Phosphorus should be applied at about 50-70 kg/ha to support overall plant health and root development. Potassium is particularly important for improving disease resistance; a dosage of 120-150 kg/ha is recommended.
                    
Calcium (Ca): Calcium helps in cell wall strengthening, which can enhance the plant's resistance to pathogens. Application rates of 100-200 kg/ha are advised, depending on soil pH and existing calcium levels.
                    
Micronutrients: Ensuring an adequate supply of micronutrients such as magnesium (Mg) and manganese (Mn) is essential for maintaining plant health and enhancing resistance to stress and disease. Typical application rates are around 10-20 kg/ha for magnesium and 5-10 kg/ha for manganese.

        """)

    elif(app_mode2=="Late_blight"):
        st.header("Late_blight")
            #image_path = "home.jpg"
            #st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
 Water-Soaked Lesions: Leaves develop dark, water-soaked spots, often at the tips or edges.

White Fungal Growth: Under humid conditions, a white fungal growth appears on the underside of the leaf lesions.
                    
Brown or Black Lesions: The spots rapidly enlarge, turning brown or black, leading to extensive leaf blight.
                    
Rapid Decay: Infected leaves and stems quickly rot, and the disease can spread to the fruit, causing dark, firm rot.
                    
Whole Plant Collapse: Severe infections can lead to the rapid collapse of the entire plant.
                    
### fertilizers
Nitrogen (N): Moderate nitrogen application is recommended to avoid lush foliage that attracts more disease. Aim for about 80-100 kg/ha, applied in split doses to balance growth.

Phosphorus (P) and Potassium (K): Adequate phosphorus and higher potassium levels can help enhance plant resistance to stress and diseases. Phosphorus should be applied at about 50-70 kg/ha and potassium at 120-150 kg/ha, depending on soil test results.
                    
Calcium (Ca): Calcium can help improve cellular structure and defense mechanisms against pathogens. Apply 100-200 kg/ha of calcium, preferably as gypsum if soil pH adjustment is not needed.
                    
Micronutrients: Ensuring a balanced supply of essential micronutrients like magnesium (Mg) and manganese (Mn) can support overall plant health. Typical application rates are about 10-20 kg/ha for magnesium and 5-10 kg/ha for manganese.

        """)

    elif(app_mode2=="Leaf_scorch"):
        st.header("Leaf_scorch")
            #image_path = "home.jpg"
            #st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
Browning Edges: Leaves typically show browning along the margins and tips which can progress inward.

Dry Patches: Affected areas are dry and crispy to the touch.
                    
Vein Confinement: The discoloration often does not cross the leaf veins at first, leading to a patterned appearance.
                    
Premature Leaf Drop: Severe scorch may cause leaves to drop prematurely.
                    
Color Variations: Depending on the plant and the severity of the stress, leaves may show yellow or red discoloration before browning.
                    
### fertilizers
                    
Moderate Nitrogen (N): Excessive nitrogen can worsen leaf scorch by encouraging tender, rapid growth that is more susceptible to damage. Aim for a conservative application, such as 50-80 kg/ha, depending on the plant and soil conditions.

Enhanced Potassium (K): Potassium plays a crucial role in improving water regulation and stress resistance in plants. Apply around 100-150 kg/ha of potassium, tailored to soil test results.
                    
Calcium (Ca): Calcium helps in strengthening cell walls, making plants more resistant to scorch symptoms. A general recommendation would be about 100-200 kg/ha, using sources like gypsum or lime, depending on soil pH.
                    
Adequate Phosphorus (P): While phosphorus doesn't need to be applied in high amounts, ensuring adequate phosphorus is important for overall health. Around 50-70 kg/ha could be beneficial.
Micronutrients: Ensure sufficient levels of micronutrients like magnesium (Mg), which is vital for chlorophyll production and overall plant vigor. Dosages around 10-20 kg/ha are advisable.

        """)

    elif(app_mode2=="Septoria_leaf_spot"):
        st.header("Septoria_leaf_spot")
            #image_path = "home.jpg"
            #st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
Small Spots: Initial symptoms are small, water-soaked spots on leaves.

Grayish Centers: These spots later develop grayish or tan centers with darker borders.
                    
Lesion Growth: As the disease progresses, the lesions may grow and merge, causing larger areas of dead tissue.
                    
Leaf Yellowing and Dropping: Infected leaves often turn yellow around the spots, eventually drying out and falling off, which can lead to significant defoliation.
                    
### fertilizers
                    
Nitrogen (N): Use nitrogen judiciously to avoid lush foliage that is more susceptible to fungal attacks. A typical application is about 80-120 kg/ha, based on the crop’s growth stage and soil fertility.

Phosphorus (P) and Potassium (K): Balanced phosphorus and enhanced potassium levels can help improve plant health and disease resistance. Apply around 50-70 kg/ha of phosphorus and 120-150 kg/ha of potassium, depending on soil test results.
                    
Calcium (Ca): Calcium can strengthen plant cell walls, potentially reducing the impact of fungal diseases. Consider applying 100-200 kg/ha of gypsum or other calcium sources.
                    
Micronutrients: Ensuring adequate levels of essential micronutrients like magnesium (Mg) and manganese (Mn) supports overall plant health. Typical applications might be 10-20 kg/ha for magnesium and 5-10 kg/ha for manganese.

        """)

    elif(app_mode2=="Two-spotted_spider_mite"):
        st.header("Two-spotted_spider_mite")
            #image_path = "home.jpg"
            #st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
                    
Speckling: Small, yellow or white spots on leaves due to mites sucking plant sap.
                    
Silk Webbing: Thin, silky webs on the leaves and between plant parts.
                    
Leaf Discoloration: Leaves may turn yellow, bronze, or even drop prematurely due to severe infestations.
                    
Stunted Growth: Heavily infested plants may exhibit reduced growth and vigor.
                    
### fertilizers
Nitrogen (N): Use moderate nitrogen levels to avoid excessive vegetative growth, which is attractive to mites. Typical dosages might range from 50 to 100 kg/ha, depending on the plant and soil conditions.

Phosphorus (P) and Potassium (K): Maintain adequate levels of phosphorus and higher levels of potassium, as potassium helps improve plant health and stress tolerance. Usual rates are about 50-70 kg/ha for phosphorus and 100-150 kg/ha for potassium.
                    
Calcium (Ca): Calcium strengthens plant tissues, making them less vulnerable to mite damage. A general recommendation is about 100-200 kg/ha, depending on soil needs.
                    
Micronutrients: Ensure plants have adequate micronutrients, particularly magnesium (Mg), which is crucial for photosynthesis and overall plant vigor. Typical magnesium application rates are around 10-20 kg/ha.

        """)

    elif(app_mode2=="Target_Spot"):
        st.header("Target_Spot")
            #image_path = "home.jpg"
            #st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
                    
Circular Spots: Initially small, water-soaked spots on leaves that expand into larger circular lesions with concentric rings, typically dark brown to black in color.

Yellow Halos: Some lesions may be surrounded by a yellow halo.
                    
Leaf Blight: As the infection progresses, leaves may yellow, wither, and drop prematurely, leading to defoliation.
                    
Fruit and Stem Lesions: On fruits and stems, dark, sunken spots can develop, which may lead to rotting.
                    
### fertilizers
                    
Nitrogen (N): Moderate nitrogen levels are crucial to avoid excessive leaf growth, which can make plants more susceptible to fungal infections. Typical application rates range from 80 to 120 kg/ha, depending on the crop and soil fertility.

Phosphorus (P) and Potassium (K): Balanced phosphorus and high potassium levels can enhance plant defense mechanisms. Apply around 50-70 kg/ha of phosphorus and 100-150 kg/ha of potassium, based on soil test results.
                    
Calcium (Ca): Calcium strengthens cell walls and can help in reducing susceptibility to fungal infections. An application rate of 100-200 kg/ha of calcium sources like gypsum might be beneficial, particularly in calcium-deficient soils.
                    
Micronutrients: Adequate supplies of micronutrients like magnesium (Mg) and manganese (Mn) are important for maintaining overall plant health. Dosages of about 10-20 kg/ha for magnesium and 5-10 kg/ha for manganese can be effective.

        """)

    elif(app_mode2=="Yellow_Leaf_Curl_Virus"):
        st.header("Yellow_Leaf_Curl_Virus")
            #image_path = "home.jpg"
            #st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
                    
Leaf Curling: Leaves begin to curl upwards and inwards, taking on a cupped shape.

Yellowing of Leaves: New growth and younger leaves may turn yellow and exhibit a reduced leaf area.
                    
Stunted Growth: Infected plants show significantly reduced growth, resulting in a stunted appearance.
                    
Flower Dropping: Flowers may fall off prematurely, severely impacting fruit set.
                    
Leaf Vein Swelling: Veins in the leaves might appear swollen and more pronounced.
                    
Reduced Fruit Size: Fruits that do develop are often smaller and fewer in number.
                    
### fertilizers
                    
Nitrogen (N): Apply nitrogen cautiously to avoid excessive growth that can attract whiteflies. A typical dosage might be 80-100 kg/ha, applied incrementally throughout the growing season.
                    
Phosphorus (P) and Potassium (K): These nutrients can help strengthen plants. Apply about 50-70 kg/ha of phosphorus and 100-120 kg/ha of potassium, adjusted based on soil test results.
                    
Calcium (Ca): Helps in strengthening cell walls, reducing vulnerability. A general recommendation is 100-200 kg/ha.
                    
Micronutrients: Ensuring adequate levels of micronutrients like magnesium and manganese can support overall plant health. Dosages around 10-20 kg/ha for magnesium and 5-10 kg/ha for manganese are typical.

        """)

    elif(app_mode2=="mosaic_virus"):
        st.header("mosaic_virus")
            #image_path = "home.jpg"
            #st.image(image_path,use_column_width=True)
        st.markdown("""
### Symptoms
Mottling: Irregular patches of light and dark green on leaves.

Leaf Distortion: Leaves may curl, wrinkle, or become puckered.
                    
Stunted Growth: Plants typically show reduced growth and development.
                    
Fruit Symptoms: Fruits may develop color breaking or become distorted, affecting their marketability.
                    
### fertilizers
                    
Balanced Fertilization: Apply a balanced N-P-K (Nitrogen, Phosphorus, Potassium) fertilizer based on soil test recommendations. Typically, a balanced application might be 120-150 kg/ha of N, 60-90 kg/ha of P, and 120-150 kg/ha of K.
                    
Micronutrients: Incorporating micronutrients such as magnesium (Mg) and zinc (Zn) can help improve overall plant health. Apply about 10-20 kg/ha of Mg and 5-10 kg/ha of Zn, based on soil deficiencies.

        """)




