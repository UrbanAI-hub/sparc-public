### Overview
This research introduces a novel way to map urban environments by combining street-level images with subjective human perceptions. By crowdsourcing visual judgments from over 1,500 participants, the resulting **Urban Space Embedding Model** learns how people actually interpret different neighborhoods. This human-centered tool provides a powerful new way to quantify and analyze the spaces we live in.

### The challenge
Traditional city maps focus on physical features like roads and buildings, missing how people actually experience a space—whether it feels safe, beautiful, or vibrant. Yet, these subjective feelings profoundly shape our mental well-being and determine how we use public areas. For a rapidly evolving city like Rotterdam, measuring these human experiences at scale remains difficult but essential. Planners need this perceptual data to design inclusive interventions, direct resources effectively, and create truly livable, people-friendly environments.

### Objectives
* **Integrate human experiences:** Embed subjective human perceptions into machine-learning models using street-level imagery.
* **Capture authentic judgments:** Collect raw, open-ended human responses through an intuitive "odd-one-out" image comparison task, rather than forcing predefined categories.
* **Map perceptual boundaries:** Classify Rotterdam's diverse urban landscape based on how people feel about spaces, offering a richer alternative to standard computer vision models.

### Approach & methodology
The researchers divided the Netherlands into small hexagonal blocks and gathered over a million street-level images. They then asked over 1,500 people to look at groups of three neighborhoods and choose the one that looked the most different. Instead of asking participants to rate areas on specific traits, this approach let the most important visual differences emerge naturally. These human choices trained a machine learning model to group perceptually similar neighborhoods together. Finally, the team applied this trained model to analyze over 7,300 specific locations across Rotterdam.

### Key findings
* **High accuracy on subjective data:** The human-guided model successfully predicted people's choices with 55% accuracy, capturing about 82% of the maximum possible accuracy for such a highly subjective task.
* **Clear performance boost:** Adding human input improved the model's ability to reflect lived experiences by 14.5% compared to standard computer-vision models.
* **Five distinct zones:** In Rotterdam, the model accurately grouped the city into five distinct perceptual zones, successfully disentangling dense commercial centers from green residential areas and suburban peripheries.

### Impact & value for the city
This perception-driven map gives city planners a new lens to view Rotterdam, revealing the subjective boundaries that separate neighborhoods. Officials can use this quantitative data to support urban renewal decisions, optimize zoning, and prioritize community investments. Ultimately, this tool helps the municipality measure the true perceptual impact of new infrastructure and ensure interventions genuinely enhance citizen well-being.
