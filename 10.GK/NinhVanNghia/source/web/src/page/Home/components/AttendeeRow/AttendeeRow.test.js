import renderer from 'react-test-renderer';

import AttendeeRow from '.';


test("It should render", async () => {
    expect(renderer.create(<AttendeeRow {...attendee}/>).toJSON()).toMatchSnapshot()
})


// ---------------------------------------------


const attendee = {
    fullname: 'Nguyen Van A',
    birthYear: 2001,
    university: 'Dai hoc BKHN',
}
