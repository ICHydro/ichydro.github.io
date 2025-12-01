---
layout: page
permalink: projects.html
style: header
---

<div class="section-title">
  <h3>Active Projects</h3>
  <div class="divider"></div>
</div>

<div class="project-gallery">
  {% for project in site.data.projects.active %}
  <div class="project-card" onclick="openProjectModal('{{ project.name | slugify }}')">
    <div class="project-logo" {% if project.logo_background %}style="background-color: {{ project.logo_background }};"{% endif %}>
      {% if project.icon %}
      <div style="font-size: 80px; color: #fed136; text-align: center; padding: 20px;">
        <i class="{{ project.icon }}"></i>
      </div>
      {% else %}
      <img src="{{ '/assets/img/' | append: project.logo | relative_url }}" alt="{{ project.name }}">
      {% endif %}
    </div>
    <div class="project-info">
      <h4>{{ project.name }}</h4>
      <p class="period">{{ project.period }}</p>
      <p class="funding">{{ project.funding }}</p>
    </div>
  </div>
  {% endfor %}
</div>

<div class="section-title">
  <h3>Past Projects</h3>
  <div class="divider"></div>
</div>

<div style="max-width: 1000px; margin: 0 auto 60px;">
  <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.8;">
    <li>2024 - 2025: FLOODTWIN - Digital twin technology for flood forecasting and management. UK NERC (£675k). Co-PI (led by Tom Coulthard, University of Hull).</li>
    <li>2018 - 2022: <a href="https://equitablehealthycities.org/">Pathways to equitable cities</a>. Wellcome Trust (£4M). Co-I (led by Majid Ezzati, Imperial College London).</li>
    <li>2019 - 2022: Water security and climate change adaptation in Peruvian glacier-fed river basins (RAHU). NERC / CONCYTEC Peru (£950k). Lead PI (jointly with Dr Pedro Rau, UTEC Peru).</li>
    <li>2019 - 2021: Understanding and managing the risk of water related diseases under hydrometeorological extremes. NERC / Malaysian Ministry of Education (£500k). Lead PI (jointly with Dr Zed Zulkafli, Universiti Putra Malaysia).</li>
    <li>2019 - 2021: Philippines Groundwater Outlook (PhiGO). NERC / Philippine Council for Industry, Energy & Emerging Technology Research & Development. (£500k). Co-I (Led by Dr Andrew Barkwith, BGS).</li>
    <li>2018 - 2022: How do the Páramos store water? The role of plants and people. NERC (£1.1M). Co-PI (Led by France Gerard, CEH).</li>
    <li>2018 - 2022: SHEAR Studentship Cohort. NERC (£1.6M). Lead PI</li>
    <li>2018 - 2022: Natural Infrastructure for Water Security. USAID & Government of Canada (US$27.5M). Co-PI (led by Forest Trends)</li>
    <li>2018 - 2022: Transforming Water, weather, and climate information through In situ observations for Geo-services in Africa (TWIGA). EU-H2020 (€ 5M). Co-PI (led by Nick van de Giesen, TUDelft).</li>
    <li>2016 - 2020: <a href="/projects/landslide-evo">Citizen science for landslide risk reduction and disaster resilience building in mountain regions</a>. UK NERC/DFID (£2M). Lead Principal Investigator.</li>
    <li>2017 - 2019: Catchment Risk Assessments using Multi-Scale Data (CARISMA). UK NERC (£200K). Co-PI (led by Geoff Parkin, University of Newcastle).</li>
    <li>2016 - 2019: Coupled Human And Natural Systems Environment (CHANSE) for water management under uncertainty in the Indo-Gangetic Plain. UK NERC (£1.25M). Co-I (led by Ana Mijic, Imperial College London).</li>
    <li>2013 - 2017: <a href="/projects/mountain-evo/">Adaptive governance of mountain ecosystem services for poverty alleviation enabled by environmental virtual observatories (MOUNTAIN-EVO)</a>. UK NERC/ESRC/DFID (£ 1.8 M). Lead Principal Investigator.</li>
    <li>2012 - 2016: Probability, Uncertainty and Risk in the Environment. UK NERC (£ 2M). Co-PI (led by Richard Chandler, University College London)</li>
    <li>2015 - 2016: Towards a high-resolution gridded precipitation product for the tropical Andes. British Council (£30k). Lead Principal Investigator.</li>
    <li>2015 - 2016: Supporting Effective Drought Risk Management in Vulnerable Catchments of Chile. British Council Newton-Picarte fund. (£23.3k). Co-I (led by Anne van Loon, University of Birmingham).</li>
    <li>2012 - 2016: <a href="/projects/hydroflux/">Hydrometeorological feedbacks and changes in water storage and fluxes in Northern India.</a> UK NERC & Indian Ministry of Earth Sciences. (£ 1.1M). Lead Principal Investigator (jointly with Pradeep Mujumdar, Indian Institute of Science, Bangalore).</li>
    <li>2014 - 2015: Using macro environmental data to support long term adaptation, management and mitigation of sustainability and climate change issues within agriculture and supply chains to the UK food retail sector. UK Technology Strategy Board (£ 185K). Co-Investigator (led by Stuart Lendrum, Sainsbury's)</li>
    <li>2011 - 2014: OASIS, Open access catastrophe modelling facility. EIT Climate - KIC (EUR 1M). Co-investigator (led by Ralf Toumi, Imperial College London).</li>
    <li>2011 - 2014: Andean Climate Change Interamerican Observatory Network. US Bureau of Western Hemisphere Affairs (USD 1M). Project partner (led by Mathias Vuille, State University New York at Albany).</li>
    <li>2010 - 2013: A UK Pilot Environmental Virtual Observatory. Natural Environment Research Council (GBP 2M). Co-PI and work package leader on environmental modelling.</li>
    <li>2011 - 2012: Smart Urban Water. EIT Climate - KIC (EUR 400K). Co-investigator (led by Nick Van de Giesen, TUDelft).</li>
    <li>2010 - 2012: Towards a Virtual Observatory for Ecosystem Services and Poverty Alleviation NERC/ESRC/DFID (GBP 250K). Lead Principal Investigator.</li>
    <li>2010 - 2011: Understanding and Managing Watershed Services in Andean and Amazonian Catchments (£50K). Co-Investigator</li>
    <li>2009 - 2010: Analysis of climate change impacts on biodiversity and the water resources in the tropical Andes. CONDESAN. Principal Investigator (USD 25K)</li>
    <li>2008 - 2009: Using remote sensing data to improve hydrological modelling of the water cycle in tropical mountain wetlands. ESA. Principal Investigator (GBP 2K)</li>
    <li>2008 - 2009: Sustainable Hydro-Energy in Patagonia. Worldbank / Universidad de Concepcion (USD 6K). Principal Investigator.</li>
    <li>2007: Participatory mapping of environmental services in the tropical Andes. Proyecto Paramo Andino. Consultant</li>
    <li>2006 - 2007: Lancaster University. Modelling wetland hydrology and the impact of human interference on its hydrological processes. European Commission, Marie Curie EIF Fellowship. Principal Investigator (EUR 141K)</li>
    <li>2005: Katholieke Universiteit Leuven and Universidad de Cuenca: Valorisation of PhD research results and structuring the research area in páramo hydrology. Flemish Interuniversitary Councel (VLIR). Principal Investigator. (EUR 5K).</li>
    <li>2004 - 2005: Katholieke Universiteit Leuven and Universidad de Cuenca: The impact of land use changes on the hydrology of the south Ecuadorian Páramo. K.U.Leuven. Coordinator.</li>
    <li>2004: Universidad de Cuenca, Ecuador: Evaluación y sistematización de mejores prácticas en el manejo de agua en los páramos de los Andes. Proyecto Páramo Andino, Quito, Ecuador. Team member.</li>
    <li>2004: Universidad de Cuenca, Ecuador: Efectos de la cobertura vegetal en la regulación hidrológica de microcuencas de páramo. Universidad de Cuenca, Ecuador. Buytaert team member</li>
    <li>2000 - 2004: Katholieke Universiteit Leuven and Universidad de Cuenca: The impact of land use changes on the hydrology of the south Ecuadorian Páramo. Fund for Scientific Research Flanders. Buytaert Coordinator.</li>
    <li>2003 - 2004: Katholieke Universiteit Leuven and Universidad de Cuenca: Participatory discussion and experimentation platform for bridging the gap between academic research and stakeholders. Flemish Interuniversitary Councel (VLIR). Buytaert team member.</li>
    <li>2003 - 2008: Katholieke Universiteit Leuven and Mekelle University: Geo-hydrology : Water resources assessment and management. Collaborative research project within the VLIR IUC cooperation with Mekelle University, Ethiopia. Buytaert team member.</li>
  </ul>
</div>

<!-- Modals for active project details -->
{% for project in site.data.projects.active %}
<div id="{{ project.name | slugify }}-modal" class="project-modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <div class="modal-project-logo" {% if project.logo_background %}style="background-color: {{ project.logo_background }};"{% endif %}>
      {% if project.icon %}
      <div style="font-size: 100px; color: #fed136; text-align: center; padding: 30px;">
        <i class="{{ project.icon }}"></i>
      </div>
      {% else %}
      <img src="{{ '/assets/img/' | append: project.logo | relative_url }}" alt="{{ project.name }}">
      {% endif %}
    </div>
    <div class="modal-project-info">
      <h3>{{ project.name }}</h3>
      <p class="period"><strong>Period:</strong> {{ project.period }}</p>
      <p class="funding"><strong>Funding:</strong> {{ project.funding }}</p>
      <p class="role"><strong>Role:</strong> {{ project.role }}{% if project.lead %} (led by {{ project.lead }}){% endif %}</p>
      <p class="description">{{ project.description }}</p>
      
      {% if project.keywords %}
      <div class="project-keywords" style="margin-top: 15px;">
        <strong>Keywords:</strong>
        <div style="margin-top: 8px;">
          {% for keyword in project.keywords %}
          <span class="badge" data-keyword="{{ keyword }}">{{ keyword }}</span>
          {% endfor %}
        </div>
      </div>
      {% endif %}
      
      {% if project.locations %}
      <div class="project-locations" style="margin-top: 15px;">
        <strong>Locations:</strong>
        <div style="margin-top: 8px;">
          {% for location in project.locations %}
          <span class="badge location-badge">{{ location }}</span>
          {% endfor %}
        </div>
      </div>
      {% endif %}
      
      {% if project.website %}
      <p class="website">
        <a href="{{ project.website }}" target="_blank" class="btn-link">
          Visit Project Website →
        </a>
      </p>
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}

<script>
function openProjectModal(projectSlug) {
  const modal = document.getElementById(projectSlug + '-modal');
  if (modal) {
    modal.classList.add('active');
  }
}

// Close modal when clicking the X or outside the modal
document.addEventListener('DOMContentLoaded', function() {
  const modals = document.querySelectorAll('.project-modal');
  
  modals.forEach(modal => {
    // Close when clicking the X
    const closeBtn = modal.querySelector('.close');
    closeBtn.addEventListener('click', function() {
      modal.classList.remove('active');
    });
    
    // Close when clicking outside the modal content
    modal.addEventListener('click', function(e) {
      if (e.target === modal) {
        modal.classList.remove('active');
      }
    });
  });
  
  // Close with ESC key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      modals.forEach(modal => {
        modal.classList.remove('active');
      });
    }
  });
});
</script>




