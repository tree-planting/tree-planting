import React, {useEffect, useState} from 'react';

import { makeStyles } from '@material-ui/core/styles';
import CircularProgress from '@material-ui/core/CircularProgress';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Link from '@material-ui/core/Link';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';

const HOME_URL = 'https://sheet2site.com/api/v3/index.php?key=1v9FhftI7hhkID2EQRhtbFc9bZ5Jq6dB89BwDh1SSCIs';

const useStyles = makeStyles((theme) => ({
  appBar: {
    backgroundColor: '#648064', //'#b3c3b3',
  },
  container: {
    marginTop: '90px',
  }
}));

/*
function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}
*/

function ContentList({data}) {
  const items = [];

  for (let d in data) {
    items.push(
        <ListItem key={d}>
        <ListItemText
          primary={d}
          secondary={data[d]}
        />
        </ListItem>
    )
  }

  return (
      <List dense={true}>
      {items}
      </List>
  )
}

export default function App() {

  const classes = useStyles();

  const [data, setData] = useState(null);

  useEffect(()=>{
    const resourceId = window.location.pathname.split('/')[2];
    const apiUrl = `${process.env.REACT_APP_API_URL}/api/place/${resourceId}/`;

    fetch(apiUrl)
      .then(res  => res.json())
      .then(
        (jd) => {
          setData(jd);
        });
  },[]);


  return (
      <React.Fragment>
      <AppBar className={classes.appBar}>
        <Toolbar>
      <Typography variant="h6"><Link href={HOME_URL} color="inherit"> 台灣好植地 Patch by Planting</Link></Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="sm" className={classes.container}>
      {(data !== null) ?
       <Box my={2}>
       <Typography variant="h4" component="h1" gutterBottom>
       {data.name}
       </Typography>
       <img src={data.cover} height="250" alt={data.name} />
       {/*<Copyright />*/}
       <ContentList data={data} />
       </Box>
       : <CircularProgress />}
      </Container>
      </React.Fragment>
  );
}
