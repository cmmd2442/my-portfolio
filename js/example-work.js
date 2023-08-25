import React from 'react';

class ExampleWork extends React.Component {

  render(){
    return (
    <section className="section section--alignCentered section--description">
      <div className="section__exampleWrapper">
        <div className="section__example">
          <img alt="example screenshot of a project involving code"
               className="section__exampleImage"
               src="images/example1.png"/>
          <dl className="color--cloud">
            <dt className="section__exampleTitle section__text--centered">
              Work Example
            </dt>
            <dd></dd>
          </dl>
        </div>
      </div>

      <div className="section__exampleWrapper">
        <div className="section__example">
          <img alt="example screenshot of a project involving chemistry"
               className="section__exampleImage"
               src="images/example2.png"/>
          <!-- “Chemistry” by Surian Soosay is licensed under CC BY 2.0
               https://www.flickr.com/photos/ssoosay/4097410999 -->
          <dl className="color--cloud">
            <dt className="section__exampleTitle section__text--centered ">
              Work Example
            </dt>
            <dd></dd>
          </dl>
        </div>
      </div>

      <div className="section__exampleWrapper">
        <div className="section__example">
          <img alt="example screenshot of a project involving cats"
               className="section__exampleImage"
               src="images/example3.png"/>
	    {/*<!-- “Bengal cat” by roberto shabs is licensed under CC BY 2.0
               https://www.flickr.com/photos/37287295@N00/2540855181 -->*/}
          <dl className="color--cloud">
            <dt className="section__exampleTitle section__text--centered">
              Work Example
            </dt>
            <dd></dd>
          </dl>
        </div>
      </div>
    </section>


    )
  }	  
}

export default ExampleWork;
